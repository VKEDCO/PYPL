#!/bin/sh

INTERACTIVE=True
ASK_TO_REBOOT=0
BLACKLIST=/etc/modprobe.d/raspi-blacklist.conf
CONFIG=/boot/config.txt

if ! [ $(id -u) = 0 ]; then
	echo "beepiutils must be run as root"
	exit 1
fi

do_expand_rootfs() {
  if ! [ -h /dev/root ]; then
    whiptail --msgbox "/dev/root does not exist or is not a symlink. Don't know how to expand" 20 60 2
    return 0
  fi

  ROOT_PART=$(readlink /dev/root)
  PART_NUM=${ROOT_PART#mmcblk0p}
  if [ "$PART_NUM" = "$ROOT_PART" ]; then
    whiptail --msgbox "/dev/root is not an SD card. Don't know how to expand" 20 60 2
    return 0
  fi

  # NOTE: the NOOBS partition layout confuses parted. For now, let's only 
  # agree to work with a sufficiently simple partition layout
  if [ "$PART_NUM" -ne 2 ]; then
    whiptail --msgbox "Your partition layout is not currently supported by this tool. You are probably using NOOBS, in which case your root filesystem is already expanded anyway." 20 60 2
    return 0
  fi

  LAST_PART_NUM=$(parted /dev/mmcblk0 -ms unit s p | tail -n 1 | cut -f 1 -d:)

  if [ "$LAST_PART_NUM" != "$PART_NUM" ]; then
    whiptail --msgbox "/dev/root is not the last partition. Don't know how to expand" 20 60 2
    return 0
  fi

  # Get the starting offset of the root partition
  PART_START=$(parted /dev/mmcblk0 -ms unit s p | grep "^${PART_NUM}" | cut -f 2 -d:)
  [ "$PART_START" ] || return 1
  # Return value will likely be error for fdisk as it fails to reload the
  # partition table because the root fs is mounted
  fdisk /dev/mmcblk0 <<EOF
p
d
$PART_NUM
n
p
$PART_NUM
$PART_START

p
w
EOF
  ASK_TO_REBOOT=1

  # now set up an init.d script
cat <<\EOF > /etc/init.d/resize2fs_once &&
#!/bin/sh
### BEGIN INIT INFO
# Provides:          resize2fs_once
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5 S
# Default-Stop:
# Short-Description: Resize the root filesystem to fill partition
# Description:
### END INIT INFO

. /lib/lsb/init-functions

case "$1" in
  start)
    log_daemon_msg "Starting resize2fs_once" &&
    resize2fs /dev/root &&
    rm /etc/init.d/resize2fs_once &&
    update-rc.d resize2fs_once remove &&
    log_end_msg $?
    ;;
  *)
    echo "Usage: $0 start" >&2
    exit 3
    ;;
esac
EOF
  chmod +x /etc/init.d/resize2fs_once &&
  update-rc.d resize2fs_once defaults &&
  if [ "$INTERACTIVE" = True ]; then
    whiptail --msgbox "Root partition has been resized.\nThe filesystem will be enlarged upon the next reboot" 20 60 2
  fi
}

kill_beePi() {
	sudo pkill -u root -f 'monitor.py'
}

if [ "$1" = "k" ] || [ "$1" = "kill" ] || [ "$1" = "-k" ] || [ "$1" = "--kill" ]; then
	echo "killing beePi monitoring processes"
	kill_beePi
	exit 0
fi

if [ "$1" = "s" ] || [ "$1" = "start" ] || [ "$1" = "-s" ] || [ "$1" = "--start" ]; then
	pgrep -u root -f 'monitor.py'
	if [ $?  = 1 ]; then
		echo "Starting monitor.py in the background"
		sudo python /home/pi/beePi/monitor.py start &
	else
		echo "Didn't start monitor.py, it's already running!"
	fi
	
	exit 0
fi

run_menu() {
choice=""

while [ "$choice" != "q" ]
do
	echo
	echo "Make a selection:"
	echo " 1) Change pi name"
	echo " 2) Set hardware clock time"
	echo " 3) Expand Filesystem"
	echo " 4) Stop beePi monitoring"
	echo " 5) Turn autostart on or off"
	echo " 6) Manually start monitoring"
	echo " 7) Archive data"
	echo " 8) Delete data"
	echo " 9) Set config to default"
	echo "10) Reboot pi"
	echo "11) Shutdown pi"
	echo " q) Quit"
	echo

	read choice
	echo

	case $choice in
		"1")
			sudo python /home/pi/beePi/manage.py -n
		;;
		"2")
			echo "The current hardware clock time is: "
			sudo hwclock -r
			echo
			echo "Would you like to change it? (y/n)"
			timeChoice=""
			read timeChoice
			echo

			if [ "$timeChoice" = "y" ]; then
				dateInput=""
				echo "Enter the current date (format: MM/DD/YYYY):"
				read dateInput
				timeInput=""
				echo
				echo "Enter the current time in 24 hour clock (format: HH:MM:SS):"
				read timeInput
				echo
				sudo hwclock --set --date "$dateInput $timeInput"
				sudo hwclock -s
				echo "The hardware clock time is now set to: "
				sudo hwclock -r
			fi
		;;
		"3")
			doubleCheck=""
			echo "Are you sure you would like to expand the filesystem? (y/n)"
			read doubleCheck

			if [ "$doubleCheck" = "y" ]; then
				do_expand_rootfs
			fi
		;;
		"4")
			shouldKill=""
			echo "This command will kill all running beePi processes, even if they are in the process of recording or transferring data."
			echo "    Are you sure you would like to stop beePi processes? (y/n)"
			read shouldKill

			if [ "$shouldKill" = "y" ]; then
				kill_beePi
			fi
		;;
		"5")
			sudo python /home/pi/beePi/manage.py -a
		;;
		"6")
			pgrep -u root -f 'monitor.py'
			if [ $?  = 1 ]; then
				runInBack=""
				echo "Run in background? (y/n/(c)ancel)"
				read runInBack

				if [ "$runInBack" = "n" ]; then
					sudo python /home/pi/beePi/monitor.py start
				elif [ "$runInBack" = "y" ]; then
					echo "Starting monitoring!"
					sudo python /home/pi/beePi/monitor.py start &
					exit
				fi
			else
				echo "Monitoring did not start: monitor.py is already running!"
			fi
		;;
		"7")
			shouldArchive=""
			echo "Are you sure you want to archive recorded data? (y/n)"
			read shouldArchive
			if [ "$shouldArchive" = "y" ]; then
				isCompressed=""
				echo "(1) Compressed archives, (2) Uncompressed archives, (c) Cancel"
				read isCompressed
				if [ "$isCompressed" = "1" ]; then
					sudo python /home/pi/beePi/manage.py -ac	
				elif [ "$isCompressed" = "2" ]; then
					sudo python /home/pi/beePi/manage.py -au
				fi
			fi
		;;
		"8")
			shouldDelete=""
			echo "Deleting recorded data should be used before making a disk image."
			echo "    Are you sure you want to delete recorded data? (y/n)"
			read shouldDelete
			if [ "$shouldDelete" = "y" ]; then
				sudo python /home/pi/beePi/manage.py -d
			fi
		;;
		"9")
			shouldReset=""
			echo "Resetting config file will set all config options to default."
			echo "    Are you sure you want to set all config to default settings? (y/n)"
			read shouldReset
			if [ "$shouldReset" = "y" ]; then
				if [ ! -f /home/pi/beePi/configDefault ]; then
					echo "No default config file found, cannot reset!"
				else
					rm /home/pi/beePi/config
					cp /home/pi/beePi/configDefault /home/pi/beePi/config
					echo "Successfully set config to default!"
				fi
			fi
		;;
		"10")
			shouldReboot=""
			echo "Are you sure you want to reboot the pi? (y/n)"
			read shouldReboot

			if [ "$shouldReboot" = "y" ]; then
				sudo reboot
			fi
		;;
		"11")
			shouldShutdown=""
			echo "Are you sure you want to shutdown the pi? (y/n)"
			read shouldShutdown

			if [ "$shouldShutdown" = "y" ]; then
				sudo shutdown now
			fi
		;;
		"q")
			echo "Quitting..."
		;;
		*)
			echo "That selection was not recognized"
		;;
	esac
done
}

run_menu

if [ "$ASK_TO_REBOOT" = 1 ]; then
	echo
	doReboot=""
	echo "Reboot pi to apply settings? (y/n)"
	read doReboot

	if [ "$doReboot" = "y" ] ; then
		echo
		echo "Rebooting..."
		sudo reboot
	fi
fi
