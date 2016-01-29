import os
import subprocess

class FileUtils:
	#creates a tar archive called "tarName".tar(.gz) by archiving all files in dataDirectory+archiveDirectoryName
	#and places the archive in dataDirectory+backupDirectoryName.
	#isCompressed is boolean that determines if method should tar.gz or normal tar
	#returns 0 if archiving was successfull, any other number otherwise
	@staticmethod
	def makeTar(tarName, dataDirectory, backupDirectoryName, archiveDirectoryName, isCompressed, logger):
		logger.log("[FileUtils] Attempting to make tar at " + os.path.join(dataDirectory,tarName+".tar"))
		try:
			if isCompressed:
				return subprocess.call(["sudo", "tar", "-cvzf", os.path.join(dataDirectory, backupDirectoryName, tarName+".tar.gz"), "-C", os.path.join(dataDirectory,archiveDirectoryName,""), "."])
			else:
				return subprocess.call(["sudo", "tar", "-cvf", os.path.join(dataDirectory, backupDirectoryName, tarName+".tar"), "-C", os.path.join(dataDirectory,archiveDirectoryName,""), "."])
		except Exception as e:
			logger.logError("FileUtils", "Error making archive", e)
	
	#counts the number of files in the specifid directory
	@staticmethod
	def countFiles(directoryFilepath):
		return len([name for name in os.listdir(directoryFilepath)])
