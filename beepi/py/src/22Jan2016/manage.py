import os
import sys
import ConfigParser
import subprocess
import time

def getTimestamp():
	return time.strftime('%Y-%m-%d_%H-%M-%S')

if __name__ == '__main__':
	usgStr = "Usage:\n    -n (change pi name),\n    -a (change autostart),\n    -ac (archive data compressed),\n    -au (archive data uncompressed),\n    -d (delete recorded data)"
	if len(sys.argv) != 2:
		print "Error: manage.py must be run with one argument"
		print usgStr
		sys.exit(1)
	if os.geteuid() != 0:
		print "Error: manage.py must be run as root!"
		sys.exit(1)
	
	arg = str(sys.argv[1])
	
	local_file_path = os.path.dirname(os.path.realpath(__file__)) + '/'
	config = ConfigParser.ConfigParser()
	cfgFile = open(local_file_path + 'config', "r")
	config.readfp(cfgFile)
	cfgFile.close()
	
	if arg == "-n":
		piName = config.get('General', 'pi_name')
		print "The current name is: " + piName
		decision = str(raw_input("   Would you like to change it? (y/n): "))

		if decision is "y":
			newName = str(raw_input("Enter a new name (No spaces please!): "))
			parsedName = newName.replace(" ", "")
			if len(newName) > 0:
				config.set("General", "pi_name", parsedName)
				cfgFileNew = open(local_file_path + 'config', "w")
				config.write(cfgFileNew)
				cfgFileNew.close()
				print "   Name was set to " + parsedName + " successfully!"
			else:
				print "   Sorry, the name you entered was not in the correct format"
	elif arg == "-a":
		autostart = config.get('General', 'auto_start')
		print "Autostart is: " + autostart
		decision = str(raw_input("Turn autostart\n    (1) on\nor\n    (2) off\n:"))

		print ""
		if decision is "1":
			config.set("General", "auto_start", "on")
			cfgFileNew = open(local_file_path + 'config', "w")
			config.write(cfgFileNew)
			cfgFileNew.close()
			print "Autostart was set to on successfully!"
		elif decision is "2":
			config.set("General", "auto_start", "off")
			cfgFileNew = open(local_file_path + 'config', "w")
			config.write(cfgFileNew)
			cfgFileNew.close()
			print "Autostart was set to off successfully!"
		else:
			print "input not recognized!"
	elif arg == "-ac" or arg == "-au":
		piName = config.get("General", "pi_name")
		
		archiveSaveSoundName = config.get("Saving", "sound_save_folder_name") + "_" + getTimestamp() + "_" + piName + "_FORCED"
		archiveSavePhotoName = config.get("Saving", "photo_save_folder_name") + "_" + getTimestamp() + "_" + piName + "_FORCED"
		
		archiveSaveDir = os.path.join(config.get("Saving", "base_data_directory"),config.get("Saving", "backup_save_folder_name"),"")
		
		archiveSaveSoundPath = os.path.join(archiveSaveDir, archiveSaveSoundName)
		archiveSavePhotoPath = os.path.join(archiveSaveDir, archiveSavePhotoName)
		
		archiveSoundReadDir = os.path.join(config.get("Saving", "base_data_directory"), config.get("Saving", "sound_save_folder_name"), "")
		archivePhotoReadDir = os.path.join(config.get("Saving", "base_data_directory"), config.get("Saving", "photo_save_folder_name"), "")
		
		if arg == "-ac":
			ret = subprocess.call(["sudo", "tar", "-cvzf", archiveSaveSoundPath+".tar.gz","-C", archiveSoundReadDir, "."])
			if ret == 0:
				os.system("sudo rm " + archiveSoundReadDir + "*")
			ret = subprocess.call(["sudo", "tar", "-cvzf", archiveSavePhotoPath+".tar.gz","-C", archivePhotoReadDir, "."]) 
			if ret == 0:
				os.system("sudo rm " + archivePhotoReadDir + "*")
		else:
			ret = subprocess.call(["sudo", "tar", "-cvf", archiveSaveSoundPath+".tar","-C", archiveSoundReadDir, "."])
			if ret == 0:
				os.system("sudo rm " + archiveSoundReadDir + "*")
			ret = subprocess.call(["sudo", "tar", "-cvf", archiveSavePhotoPath+".tar","-C", archivePhotoReadDir, "."])
			if ret == 0:
				os.system("sudo rm " + archivePhotoReadDir + "*")
	elif arg == "-d":
		baseDir = config.get("Saving", "base_data_directory")
		soundPath = os.path.join(baseDir, config.get("Saving", "sound_save_folder_name"), "")
		photoPath = os.path.join(baseDir, config.get("Saving", "photo_save_folder_name"), "")
		backupPath = os.path.join(baseDir, config.get("Saving", "backup_save_folder_name"), "")
		
		os.system("sudo rm " + soundPath + "*")
		os.system("sudo rm " + photoPath + "*")
		os.system("sudo rm " + backupPath + "*")
		
		for f in os.listdir(baseDir):
			fp = os.path.join(baseDir, f)
			if os.path.isfile(fp):
				os.remove(fp)
				os.system("touch " + fp)
	else:
		print usgStr
		sys.exit(1)
	
	sys.exit(0)
