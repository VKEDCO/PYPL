import os
import threading
import time

from FileOperations import FileOperations
from TimeUtils import TimeUtils

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
#def getTimestamp():
#	return time.strftime('%Y-%m-%d_%H-%M-%S')
	
#class that is used to record data at a specified interval
#tempReadFile is linux system file that is read to determine temperature, determined by parseConfig method
#saves data at tempSaveDirectory+tempSaveFilename
#interval is time in seconds between sampling data
class TemperatureReader:
	def __init__(self, tempReadFile, tempSaveDirectory, tempSaveFilename, interval):
		self.temperatureReadFile = tempReadFile
		self.temperatureSaveFile = os.path.join(tempSaveDirectory,tempSaveFilename)
		self.sampleInterval = interval
		self.isRecording = False
		self.recordingLoopActive = False
		self.threadsStarted = False
		self.nextTimer = None
		self.tempLogger = FileOperations(tempSaveDirectory, tempSaveFilename)
	
	#starts recording temperature at specified interval
	def startRecording(self):
		self.recordingLoopActive = True
		if(self.threadsStarted == False):
			threading.Timer(0, self.sampleTemperatureWithInterval, ()).start()
			self.threadsStarted = True
	
	#requests recording thread to stop+pi-
	def stopRecording(self):
		self.recordingLoopActive = False
	
	#used to force the thread to stop recording if there was an error in recording data
	def resetIsRecording(self):
		self.isRecording = False
	
	#this method is called by timer threads to record data at the specified interval
	def sampleTemperatureWithInterval(self):
		#launching next timer thread to record temp after specified interval
		self.nextTimer = threading.Timer(self.sampleInterval, self.sampleTemperatureWithInterval, ())
		self.nextTimer.start()
		if(self.recordingLoopActive == True and self.storage.hasSpace()):
			self.isRecording = True
			#line below ensures that, even when there is an error recording temperature, isRecording won't stay on
			#The pi has 10 seconds to record temperature
			threading.Timer(10, self.resetIsRecording, ()).start()
			try:
				temperature = self.readTemperature()
				timestamp = TimeUtils.getTimestamp()
				output = "%s %s\n" % (timestamp, temperature)
				#adding temperature to temperature file
				self.tempLogger.appendToFile(output)
				self.logger.log("[TemperatureReader] Recorded temperature")
			except Exception as e:
				self.logger.logError("TemperatureReader", "Error reading temperature", e)
			self.isRecording = False
	
	#parses system file to get temperature in Celcuis
	def readTemperature(self):
		with open(self.temperatureReadFile, 'r') as temperatureFile:
			text = temperatureFile.read()
			secondLine = text.split('\n')[1]
			temperatureData = secondLine.split(' ')[9]
			temperature = float(temperatureData[2:])
			return temperature/1000
	
	#cancels any timers that are waiting to excecute. Used when quitting the program
	def quit(self):
		if self.nextTimer != None:
			self.nextTimer.cancel()
			
	def setLogger(self, logger):
		self.logger = logger
		
	def setStorage(self, storage):
		self.storage = storage
