import time

from TemperatureReader import TemperatureReader
from PictureReader import PictureReader
from SoundReader import SoundReader

#Manages the starting and stopping of recording threads
#Currently, it only manages sound, temperature, and picture threads, but any
#other data recording threads that are to be added later should be added to this class
class RecordingManager:
	#uses config map to setup recording threads
	def __init__(self, config, logger, storage):
		self.temperatureReader = TemperatureReader(config['temperature_read_file'], config['base_data_directory'], config['temperature_save_file'], config['temperature_sampling_interval'])
		self.pictureReader = PictureReader(config['photo_save_folder'], config['picture_sampling_interval'])
		self.soundReader = SoundReader(config['sound_save_folder'], config['sound_sampling_interval'], config['sound_sample_length'])
		self.soundTime = config['sound_sample_length'];
		
		self.temperatureReader.setLogger(logger)
		self.temperatureReader.setStorage(storage)
		
		self.pictureReader.setLogger(logger)
		self.pictureReader.setStorage(storage)
		
		self.soundReader.setLogger(logger)
		self.soundReader.setStorage(storage)
		
		self.logger = logger
	
	#starts all recording threads
	def startRecording(self):
		self.logger.log("[RecordingManager] starting recording threads")
		self.temperatureReader.startRecording()
		self.pictureReader.startRecording()
		self.soundReader.startRecording()
		self.logger.log("[RecordingManager] threads started")
	
	#requests that all recording threads stop, and waits for all of them to stopshop
	def stopRecording(self):
		self.logger.log("[RecordingManager] stopping recording threads")
		#requesting threads to stop
		self.temperatureReader.stopRecording()
		self.pictureReader.stopRecording()
		self.soundReader.stopRecording()
		
		self.logger.log("[RecordingManager] waiting for threads to stop...")
		
		#waiting for all threads to stop
		counter = 0
		while self.temperatureReader.isRecording or self.pictureReader.isRecording or self.soundReader.isRecording:
			counter += 1
			if counter > (self.soundTime + 10):
				#sound thread should have stopped by now if we end up here, because we waited for
				#more seconds than it is supposed to be recording
				logger.log("[RecordingManager] Sound thread did not quit, cannot stop recording")
				return False #stop was unsucessful
			time.sleep(1)
		
		#one more request to stop recording, just to be safe
		self.temperatureReader.stopRecording()
		self.pictureReader.stopRecording()
		self.soundReader.stopRecording()
		self.logger.log("[RecordingManager] threads stopped")
		return True #stop was sucessfull
	
	#makes all threads quit, used when quitting the application
	def quitThreads(self):
		self.stopRecording()
		self.pictureReader.quit()
		self.soundReader.quit()
		self.temperatureReader.quit()
	
