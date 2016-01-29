import os

#Utility class to check if there is enough free space to record data
class Storage:
	def __init__(self):
		#this should be set in __main__ once we get min_free_mb from config
		self.minFreeMB = 700
		
	def hasSpace(self):
		s = os.statvfs("/")
		#free space in bytes, divided by bytes in a MB (1024^2)
		spaceRem = int((s.f_bavail * s.f_frsize)/(1024**2))
		if spaceRem < self.minFreeMB:
			logger.log("[Storage] There isn't enough free space to save data!")
			return False
		else:
			return True
	
	def setLogger(self, logger):
		self.logger = logger
