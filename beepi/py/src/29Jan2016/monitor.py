import ConfigParser
import os
import time
import threading
import pyaudio
import wave
import signal
import sys
import picamera
import filelock
#import socket
#import Queue
import RPi.GPIO as GPIO
#from ftplib import FTP
#from fnmatch import fnmatch
#from subprocess import call
#from subprocess import check_output
#from subprocess import CalledProcessError

from FileOperations import FileOperations
from Storage import Storage
#from TemperatureReader import TemperatureReader
#from PictureReader import PictureReader
#from SoundReader import SoundReader
#from FileUtils import FileUtils
#from NetworkUtils import NetworkUtils
from RecordingManager import RecordingManager
from ArchiveManager import ArchiveManager
#from UDPReceiver import UDPReceiver
from FtpConnector import FtpConnector

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
#def getTimestamp():
#	return time.strftime('%Y-%m-%d_%H-%M-%S')


#utility method to set up GPIO used by sensors attached to the pi
#called at the beginning of __main__
def setupGPIO():
	os.system("sudo modprobe w1-therm")
	os.system("sudo modprobe w1-gpio")
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)


#need to set up filepath and filename when we get config in __main__
#used for all classes and threads in this file for logging purposes
logger = FileOperations()

#Need to setup actual minFreeMB once we get config data in __main__
#used by recording threads to check if there is enough room on the pi to record data
storage = Storage()
storage.setLogger(logger)

#parses data in config file and returns a map of data entries to values
def readConfig():
	configDict = {}
	
	#finding and opening config file
	#parses config file with built in python config parser
	local_file_path = os.path.dirname(os.path.realpath(__file__)) + '/'
	config = ConfigParser.ConfigParser()
	config.readfp(open(local_file_path + 'config'))
	
	base_data_directory = os.path.join(config.get('Saving', 'base_data_directory'), "")
	
	configDict['base_data_directory'] = base_data_directory

	#searching for the correct temperature read file
	#changes with each sensor (has different serial num)
	pathBefore = '/sys/bus/w1/devices/' #should always be consistent
	pathEnd = 'w1_slave'
	files = []
	for i in os.listdir(pathBefore):
		f = os.path.join(pathBefore, i, pathEnd)
		if os.path.isfile(f) and '28' in i and len(i) == 15:
			files.append(f)
	
	configDict['temperature_read_file'] = files[0]
	configDict['temperature_save_file'] = config.get('Saving', 'temperature_save_filename')
	configDict['log_save_file'] = config.get('Saving', 'log_save_filename')
	
	configDict['pi_name'] = config.get('General', 'pi_name')
	
	if config.get('Saving', 'use_compressed_archives') == 'y':
		configDict['use_compressed_archives'] = True
	else:
		configDict['use_compressed_archives'] = False
	
	configDict['photo_save_folder_name'] = config.get('Saving', 'photo_save_folder_name')
	configDict['sound_save_folder_name'] = config.get('Saving', 'sound_save_folder_name')
	configDict['backup_save_folder_name'] = config.get('Saving', 'backup_save_folder_name')
	
	#creating save directories and files if they do not exist already
	configDict['photo_save_folder'] = os.path.join(base_data_directory,config.get('Saving', 'photo_save_folder_name'),"")
	configDict['sound_save_folder'] = os.path.join(base_data_directory,config.get('Saving', 'sound_save_folder_name'),"")
	configDict['backup_save_folder'] = os.path.join(base_data_directory,config.get('Saving', 'backup_save_folder_name'),"")
	if not os.path.exists(os.path.join(configDict['base_data_directory'],configDict['temperature_save_file'])):
		f = file(os.path.join(configDict['base_data_directory'],configDict['temperature_save_file']), "w")
		f.close()
	if not os.path.exists(os.path.join(configDict['base_data_directory'],configDict['log_save_file'])):
		f = file(os.path.join(configDict['base_data_directory'],configDict['log_save_file']), "w")
		f.close()
	if not os.path.exists(configDict['photo_save_folder']):
		os.makedirs(configDict['photo_save_folder'])
	if not os.path.exists(configDict['sound_save_folder']):
		os.makedirs(configDict['sound_save_folder'])
	if not os.path.exists(configDict['backup_save_folder']):
		os.makedirs(configDict['backup_save_folder'])
	
	configDict['temperature_sampling_interval'] = int(config.get('Sampling', 'temperature_sampling_interval'))
	configDict['sound_sampling_interval'] = int(config.get('Sampling','sound_sampling_interval'))
	configDict['sound_sample_length'] = int(config.get('Sampling','sound_sample_length'))
	configDict['picture_sampling_interval'] = int(config.get('Sampling','picture_sampling_interval'))
	
	configDict['server_ip'] = config.get('General','server_ip')
	configDict['backup_server_ip'] = config.get('General','backup_server_ip')
	
	configDict['udp_port'] = config.get('General', 'udp_port')
	configDict['ftp_simple_port'] = config.get('General', 'ftp_simple_port')
	configDict['ftp_advanced_port'] = config.get('General', 'ftp_advanced_port')
	
	configDict['ftp_user'] = config.get('General', 'ftp_user')
	configDict['ftp_password'] = config.get('General', 'ftp_password')

	configDict['auto_start'] = config.get('General', 'auto_start')
	
	configDict['min_free_mb'] = int(config.get('General', 'min_free_mb'))
	
	configDict['archive_file_count'] = int(config.get('Saving', 'archive_file_count'))
	configDict['archive_check_interval'] = int(config.get('Saving', 'archive_check_interval'))
	
	return configDict

		
if __name__ == '__main__':
	#we can force monitor.py to start even if autostart is turned off, buy giving it the single argument "start"
	forceStart = False
	if len(sys.argv) == 2:
		startArg = str(sys.argv[1])
		if startArg == "start":
			forceStart = True
	
	#performing initial setup
	setupGPIO()
	config = readConfig()
	
	#finishing the setup of objects instanciated before __main__
	logger.setSaveLocation(config['base_data_directory'], config['log_save_file'])
	storage.minFreeMB = config['min_free_mb']
	
	#checking if we have to stop due to autostart
	if config['auto_start'] == "off" and not forceStart:
		logger.log("[__main__] Quitting application: auto_start and force start disabled")
		sys.exit(0)
	#checking if the user is root, and stopping if they aren't
	if os.geteuid() != 0:
		logger.log("[__main__] Error: monitor.py must be run as root!")
		sys.exit(1)
	
	#setting up all manager objects below (recordingManager, archiveManager, ftpConnector)
	#they should all behave autonomously until the program stops
	recordingManager = RecordingManager(config, logger, storage)
	
	logger.log("[__main__] setup complete, starting recording")
	recordingManager.startRecording()
	
	logger.log("[__main__] starting archive thread")
	archiveManager = ArchiveManager(config, recordingManager, logger)
	archiveManager.startArchiving()
	
	logger.log("[__main__] starting FTP search thread")
	ftpConnector = FtpConnector(config, recordingManager, archiveManager, logger)
	ftpConnector.startSearching()
	
	#Handles ctrl-c when not running in the background
	#this is buggy and doesn't work a log or the time
	#better to stop the program with "beepiutils k" for now
	while True:
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			break
	
	#quitting all threads
	ftpConnector.quit()
	archiveManager.quit()
	recordingManager.quitThreads()
	
