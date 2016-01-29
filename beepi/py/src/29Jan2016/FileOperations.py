import os
import filelock
#import time

from TimeUtils import TimeUtils

#utility method to get the current timestamp in a format that
#can be used as a valid filename in Windows and Linux/Unix
#VK: Placed inside TimeUtils
#def getTimestamp():
#	return time.strftime('%Y-%m-%d_%H-%M-%S')

#FileOperations is used to append to a file in a thread safe manner. Useful for logging
#or adding data to a text file
class FileOperations:
	#Constructor can be used without parameters. Just set them later.
	#Until you set a filename and filepath, methods will print to console only
	def __init__(self, filepath=None, filename=None):
		self.filepath = None
		self.filename = None
		if(filepath != None and filename != None):
			self.setSaveLocation(filepath, filename)
	#Used to set save location after construction, or used during construction if parameters are provided
	def setSaveLocation(self, filepath, filename):
		#There is an error state where the lockfile stays locked until it is deleted.
		#This happens when the program shuts down while FileOperations is appending to a file
		#To fix this problem we delete the lock file when we construct the object and create a new one
		lockFilePath = os.path.join(filepath,filename+"lockfile")
		if os.path.isfile(lockFilePath):
			os.remove(lockFilePath)
		if not os.path.isfile(os.path.join(filepath,filename)):
			tempFile = open(os.path.join(filepath,filename), "w+")
			tempFile.close()
		self.filepath = filepath
		self.filename = filename
		#lock is used so only one thread can write to the file at a time
		#filelock is a third party library, install with pip if you don't have it
		self.lock = filelock.FileLock(lockFilePath)
	#locks the file so only one thread can access it, then appends to it. No timestamps or newlines added
	def appendToFile(self, text):
		if self.filepath is None:
			return
		with self.lock:
			f = open(os.path.join(self.filepath,self.filename), 'a')
			f.write(text)
			f.close()
	#prints to console and appends to file on a new line with timestamp
	def log(self, text):
		#logText is printed to console and file
		logText = TimeUtils.getTimestamp() + " " + text
		print logText
		if self.filepath is not None:
			self.appendToFile(logText + "\n")
	#Logs error messages from exceptions in a nicely formatted manner. Class name is the class you
	#are in while the error occurs.
	def logError(self, className, msg, e):
		startString = "["+className+"] "
		self.log(startString+msg)
		#prints exception info if possible
		errorStr = repr(e)
		if errorStr is not None:
			self.log(startString + "ERROR: " + errorStr)
		errStrClass = e.__class__.__name__
		if errStrClass is not None:
			self.log(startString + "ERROR CLASS: " + errStrClass)
	#Moves the file into the specified path with the specified new name, and creates a new empty file
	#with the same name and path as the file before it was moved
	def makeBackup(self, newFilepath, piName):
		if self.filepath is None:
			return
		#need a lock so no thread writes to file while we are moving it and creating a new one
		with self.lock:
			os.rename(os.path.join(self.filepath,self.filename), os.path.join(newFilepath,self.filename.split(".")[0] + \
				 "_" + TimeUtils.getTimestamp() + "_" + piName + ".txt"))
			tempFile = open(os.path.join(self.filepath,self.filename), "w+")
			tempFile.close()
