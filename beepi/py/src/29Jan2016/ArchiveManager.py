import os
import time
import threading
from FileUtils import FileUtils
from TimeUtils import TimeUtils

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
#def getTimestamp():
#	return time.strftime('%Y-%m-%d_%H-%M-%S')

#after a specified interval (in config map) checks if there are enough files to archive into tar files
#if there are enough files, stops recording threads and archives the files. This may take some time
class ArchiveManager:
	def __init__(self, config, recordingManager, logger):
		self.recordingManager = recordingManager
		self.useCompressed = config['use_compressed_archives']
		self.fileCount = config['archive_file_count'] #need this many files in a folder to archive it
		self.soundDirectory = config['sound_save_folder']
		self.pictureDirectory = config['photo_save_folder']
		self.soundDirectoryName = config['sound_save_folder_name']
		self.pictureDirectoryName = config['photo_save_folder_name']
		self.piName = config['pi_name']
		self.baseDataDirectory = config['base_data_directory']
		self.backupDirectory = config['backup_save_folder_name']
		#seconds in between archive checks
		self.checkInterval = config['archive_check_interval'] #interval for checking if it is time to archive
		self.nextTimer = None
		self.isProcessing = False
		self.hasStarted = False
		self.keepArchiving = False
		self.logger = logger
	
	#starts thread that checks if it is time to archive, every self.checkInterval seconds
	def startArchiving(self):
		self.keepArchiving = True
		self.logger.log("[ArchiveManager] starting archiving threads")
		if not self.hasStarted:
			self.nextTimer = threading.Timer(0, self.archiveCheck, ())
			self.nextTimer.start()
			self.hasStarted = True
	
	#waits for archiving to stop. This may take some time if it is currently archiving a large folder
	def stopArchiving(self):
		self.keepArchiving = False
		#wainting for archiving in process to stop
		self.logger.log("[ArchiveManager] stopping archiving threads")
		while self.isProcessing: #keep checking if the archivingThread is currently processing a tar file
			time.sleep(1)
		self.keepArchiving = False #prevents the archiveManager from making more archives until we call the startArchiving() method
		return
	
	#checks if the folder specified by the filepath has enough files to archive, returns boolean
	def shouldArchive(self, directoryFilepath):
		fileCount = FileUtils.countFiles(directoryFilepath)
		self.logger.log("[ArchiveManager] Found " + str(fileCount) + " files in " + directoryFilepath)
		return FileUtils.countFiles(directoryFilepath) >= self.fileCount
	
	#calls FileUtils static class to archive the files
	def makeArchive(self, directoryName, name):
		return FileUtils.makeTar(name, self.baseDataDirectory, self.backupDirectory, directoryName, self.useCompressed, self.logger)
	
	#method called by archive timers to archive files, if there are enough files to archive
	def archiveCheck(self):
		if self.keepArchiving:
			self.isProcessing = True
			#checking if there are enough files to archive
			shouldArchiveSound = self.shouldArchive(self.soundDirectory)
			shouldArchivePictures = self.shouldArchive(self.pictureDirectory)
		
			#if there aren't enough files to archive, we do nothing
			if not shouldArchiveSound and not shouldArchivePictures:
				self.nextTimer = threading.Timer(self.checkInterval, self.archiveCheck, ())
				self.nextTimer.start()
				self.logger.log("[ArchiveManager] not enough files to archive, exiting")
				self.isProcessing = False
				return
			
			#if there are enough files, we ask recordingManager to stop recording threads
			#if it wasn't able to stop the recording threads, we enter this if statement, and do nothing because
			#we couldn't stop the recording threads
			if not self.recordingManager.stopRecording():
				self.nextTimer = threading.Timer(self.checkInterval, self.archiveCheck, ())
				self.nextTimer.start()
				self.logger.log("[ArchiveManager] could not stop recordings, exiting")
				self.recordingManager.startRecording()
				self.isProcessing = False
				return
		
			#if there are enough sound files to archive, we enter this if block and attempt to archive the sound files
			if shouldArchiveSound:
				self.logger.log("[ArchiveManager] Attempting to archive sound")
				try:
					self.logger.log("[ArchiveManager] Making sound archive")
					#if makeArchive fails, it will return non 0 value and we will not delete old sound files
					if self.makeArchive(self.soundDirectoryName, self.soundDirectoryName + '_'+ TimeUtils.getTimestamp() + '_' +self.piName) == 0:
						self.logger.log("[ArchiveManager] Removing old sound files")
						#tries to remove all .wav and .mp3 files from the folder
						try:
							os.system("sudo rm " + self.soundDirectory + "*.wav")
						except Exception as e:
							self.logger.logError("ArchiveManager", "Error removing .wav files", e)
						
						try:
							os.system("sudo rm " + self.soundDirectory + "*.mp3")
						except Exception as e:
							self.logger.logError("ArchiveManager", "Error removing .mp3 files", e)
					else:
						self.logger.log("[ArchiveManager] Sound archive was not created, exit code was not 0")
				except Exception as e:
					self.logger.logError("ArchiveManager", "Error making sound archive", e)
			
			#if there are enough picture files to archive, we enter this if block and attempt to archive the picture files
			if shouldArchivePictures:
				self.logger.log("[ArchiveManager] Attempting to archive photos")
				try:
					self.logger.log("[ArchiveManager] Making photo archive")
					#if makeArchive fails, it will return non 0 value and we won't delete old photos
					if self.makeArchive(self.pictureDirectoryName, self.pictureDirectoryName+'_'+ TimeUtils.getTimestamp()+'_'+self.piName) == 0:
						self.logger.log("[ArchiveManager] Removing old picture files")
						#removes all .png files
						try:
							os.system("sudo rm " + self.pictureDirectory+"*.png")
						except Exception as e:
							self.logger.logError("ArchiveManager", "Error removing .png files", e)
						else:
							self.logger.log("Photo archive was not created, exit code was not 0")
				except Exception as e:
						self.logger.logError("ArchiveManager", "Error making picture archive", e)
		
			#we are done archiving files, so we tell the recordingManager to start recording again
			self.recordingManager.startRecording()
			#set isProcessing to False to show that we are done archiving
			self.isProcessing = False
		
		#launches next archive timer thread
		self.nextTimer = threading.Timer(self.checkInterval, self.archiveCheck, ())
		self.nextTimer.start()
	
	#cancels or stops all archiving threads to quit the application
	def quit(self):
		self.stopArchiving()
		self.nextTimer.cancel()
