import subprocess
 
#static class containing utilities for dealing with networking
class NetworkUtils:
	#checks if pi is connected to a network with the name "name"
	#NOTE: the pi will automatically connect to networks it finds that match the network in /etc/wpa_supplicant/wpa_supplicant.conf
	@staticmethod
	def isConnectedToNetwork(name):
		try:
			#system call returns the ssid of currently connected network
			return (name == subprocess.check_output(["iwgetid", "-r"]).strip())
		except subprocess.CalledProcessError:
			return False

	#gets the signal strength of the currently connected network, as a float from 0.0 to 1.0
	#returns 0 if not connected to network
	@staticmethod
	def getSignalStrength():
		#parses /proc/net/wireless to find signal strength
		strengthString = subprocess.check_output(["awk", "NR==3 {print $3}", "/proc/net/wireless"]).strip()
		if strengthString == "":
			return 0
		strengthString = strengthString.replace(".", "")
		return float(strengthString)/70.0
