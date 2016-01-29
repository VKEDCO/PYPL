import time

class TimeUtils:
	#utility method to get the current timestamp in a format that
	#can be used as a valid filename in Windows and Linux/Unix
	@staticmethod
	def getTimestamp():
		return time.strftime('%Y-%m-%d_%H-%M-%S')
