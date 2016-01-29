import os
import threading
import time
import picamera

from FileOperations import FileOperations
from TimeUtils import TimeUtils

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
#def getTimestamp():
#	return time.strftime('%Y-%m-%d_%H-%M-%S')

#Records pictures at the specified interval
#arguments are the filepath to the folder that will contain the pictures, and the interval to record the pictures in seconds
class PictureReader:
	def __init__(self, picSaveFolder, interval):
		self.saveFolder = picSaveFolder
		self.sampleInterval = interval
		self.isRecording = False
		self.recordingLoopActive = False
		self.threadsStarted = False
		self.nextTimer = None
	
	#starts taking pictures on the specified interval
	def startRecording(self):
		self.recordingLoopActive = True
		if(self.threadsStarted == False):
			threading.Timer(0, self.samplePictureWithInterval, ()).start()
			self.threadsStarted = True
	
	#requests that the Picture reader stop recording data
	def stopRecording(self):
		self.recordingLoopActive = False
	
	#used in case of error with stopping recording
	def resetIsRecording(self):
		self.isRecording = False
	
	#called by timer threads to sample the temperature
	def samplePictureWithInterval(self):
		#setting up the next timer thread
		self.nextTimer = threading.Timer(self.sampleInterval, self.samplePictureWithInterval, ())
		self.nextTimer.start()
		if (self.recordingLoopActive == True and self.storage.hasSpace()):
			self.isRecording = True
			#line below ensures that, even when there is an error taking a picture, isRecording won't stay on
			#The pi has 15 seconds to take the picture
			threading.Timer(15, self.resetIsRecording, ()).start()
			timestamp = TimeUtils.getTimestamp()
			try:
				self.takePicture(self.saveFolder, timestamp+'.png')
				self.logger.log("[PictureReader] Took picture")
			except Exception as e:
				self.logger.logError("PictureReader", "Error taking picture", e)
			self.isRecording = False
	
	#takes a picture and saves it on the specified filepath with the specified filename
	def takePicture(self, filepath, filename):
		with picamera.PiCamera() as camera:
			camera.capture(os.path.join(filepath,filename))
	
	#cancels recording thread, used when quitting the program
	def quit(self):
		if self.nextTimer != None:
			self.nextTimer.cancel()
			
	def setLogger(self, logger):
		self.logger = logger
		
	def setStorage(self, storage):
		self.storage = storage
