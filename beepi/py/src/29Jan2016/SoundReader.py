import os
import threading
import time

from FileOperations import FileOperations

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
def getTimestamp():
	return time.strftime('%Y-%m-%d_%H-%M-%S')

#Samples audio after interval seconds with length seconds and saves it at soundSaveFolder
class SoundReader:
	def __init__(self, soundSaveFolder, interval, length):
		self.saveFolder = soundSaveFolder
		self.sampleInterval = interval
		self.sampleLength = length
		self.isRecording = False
		self.recordingLoopActive = False
		self.threadsStarted = False
		self.nextTimer = None
	
	#starts recording threads
	def startRecording(self):
		self.recordingLoopActive = True
		if(self.threadsStarted == False):
			threading.Timer(0, self.sampleAudioWithInterval, ()).start()
			self.threadsStarted = True
	
	#requests that the threads stop recording
	def stopRecording(self):
		self.recordingLoopActive = False
	
	#used if there is an error with stopping the recording thread
	def resetIsRecording(self):
		self.isRecording = False
	
	#called by timers to sample audio after interval seconds
	def sampleAudioWithInterval(self):
		#setting up next recording timer thread
		self.nextTimer = threading.Timer(self.sampleInterval, self.sampleAudioWithInterval, ())
		self.nextTimer.start()
		if(self.recordingLoopActive == True and self.storage.hasSpace()):
			self.isRecording = True
			#line below ensures that, even when there is an error recording sound, isRecording won't stay on
			#The pi has 15 seconds more than the sample length to finish saving the data
			threading.Timer(self.sampleLength + 15, self.resetIsRecording, ()).start()
			timestamp = getTimestamp()
			try:
				self.logger.log("[SoundReader] Started recording audio")
				self.recordAudio(self.sampleLength, self.saveFolder, timestamp+'.mp3')
				self.logger.log("[SoundReader] Recorded audio")
			except Exception as e:
				self.logger.logError("SoundReader", "Error recording sound", e)
			self.isRecording = False
	
	#records audio sampleSeconds long and saves it to filepath folder with filename
	def recordAudio(self, sampleSeconds, filepath, filename):
		recordString = self.getRecordString(sampleSeconds, filepath, filename)
		#excecutes system call
		os.system(recordString)
		
	#gets the string used as system call to record audio
	def getRecordString(self, sampleSeconds, filepath, filename):
		#records raw audio with arecord and pipes it to lame mp3 encoder to convert to mp3
		#edit "--preset medium -mm" section if you would like to change recorded audio quality
		#learn about presets by calling "man lame" in console
		return "arecord -f cd -d " + str(sampleSeconds) + " -t wav | lame --preset medium -mm - " + os.path.join(filepath,filename)
	
	#cancels recording threads, used when quitting application
	def quit(self):
		if self.nextTimer != None:
			self.nextTimer.cancel()
			
	def setLogger(self, logger):
		self.logger = logger
		
	def setStorage(self, storage):
		self.storage = storage
