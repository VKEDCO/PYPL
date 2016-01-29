import time
import threading
import socket
import subprocess
import os
 
from NetworkUtils import NetworkUtils
from UDPReceiver import UDPReceiver
from ftplib import FTP

#this tries to find an FTP server every interval seconds
#if FTP is found and login is successfull, it stops all archiving and recording threads while it attempts to send the data
#after that, it resumes archiving and recording threads
class FtpConnector:
	def __init__(self, config, recordingManager, archiveManager, logger):
		self.recordingManager = recordingManager
		self.archiveManager = archiveManager
		self.user = config['ftp_user']
		self.pwd = config['ftp_password']
		self.ip = config['server_ip']
		self.backupIp = config['backup_server_ip']
		self.simplePort = config['ftp_simple_port']
		self.advancedPort = config['ftp_advanced_port']
		self.udpPort = config['udp_port']
		self.dataDirectory = config['base_data_directory']
		self.backupFolder = config['backup_save_folder']
		self.piName = config['pi_name']
		self.isProcessing = False
		self.keepSearching = False
		self.nextTimer = None
		self.checkInterval = 10
		self.sendAlive = False
		self.logger = logger
	
	#starts searching for FTP server every interval seconds
	def startSearching(self):
		self.logger.log("[FtpConnector] Starting FTP server search")
		self.keepSearching = True
		if self.nextTimer is None:
			self.nextTimer = threading.Timer(0, self.trySendData, ())
			self.nextTimer.start()
	
	#stops searching for FTP threads. Waits for current FTP transfers to finish before returning
	def stopSearching(self):
		self.logger.log("[FtpConnector] Stopping FTP server search")
		self.keepSearching = False
		while self.isProcessing:
			time.sleep(1)
		return
	
	#stops or cancels all FTP threads to quit the application
	def quit(self):
		self.logger.log("[FtpConnector] Quitting FTP server search")
		self.stopSearching()
		while self.isProcessing:
			time.sleep(1)
		self.nextTimer.cancel()
		return
	
	#this method is called by FTP searching threads. If we are connected to the BeePiWifi network
	#it attempts to connect to a variety of FTP servers on that network and transfers data to the
	#first FTP server it is able to connect to
	def trySendData(self):
		if self.keepSearching:
			#resets checkInterval to 10 seconds in a variety of places
			#if an FTP transfer completes, the check interval is set to 900 seconds elsewhere in the class because
			#we don't want to keep connecting to the server over and over again if we have already transfered to it
			self.checkInterval = 10
			try:
				signalStrength = NetworkUtils.getSignalStrength()
				isConnected = NetworkUtils.isConnectedToNetwork("BeePiWifi")
				if isConnected and signalStrength > .25:
					#if we are connected to BeePiWifi and the signal strength is greater than 25%, we try to find an FTP server
					self.logger.log("[FtpConnector] Signal strength check: " + str(signalStrength))
					self.logger.log("[FtpConnector] Is Connected: " + str(isConnected))
					self.logger.log("[FtpConnector] Attempting to connect to FTP server")
					#calls method that attempts find FTP servers on the network
					self.connectToServer()
			except Exception as e:
				self.logger.logError("FtpConnector", "Error checking network", e)
				self.checkInterval = 10
		
		#cleans up after performing operations
		self.sendAlive = False
		self.nextTimer = threading.Timer(self.checkInterval, self.trySendData, ())
		self.nextTimer.start()
	
	#attempts to connect to FTP server on network. If successful, data is transfered to the connected server
	#FTP server connection priority: Advanced, Simple, Simple Backup
	def connectToServer(self):
		isConnected = True
		
		ftp = FTP()
		try:
			#tries to connect to Advanced FTP server. If not successful, tries to connect to simple FTP server
			self.logger.log("[FtpConnector] Attepting to connect to advanced FTP server with:")
			self.logger.log("[FtpConnector] IP "+self.ip+", port "+self.advancedPort+", user "+self.user+", pwd "+self.pwd)
			ftp.connect(self.ip, self.advancedPort, 10)
			self.logger.log("[FtpConnector] Logging in to FTP server")
			ftp.login(self.user, self.pwd)
			self.sendFilesAdvanced(ftp)
		except Exception as e:
			isConnected = False
			self.logger.logError("FtpConnector", "Error logging into advanced ftp server, attempting to connect to simple FTP server", e)
			
		if isConnected:
			return
		
		isConnected = True
		try:
			#tries to connect to Simple FTP server. If not successful, tries to connect to simple backup FTP server
			self.logger.log("[FtpConnector] Attepting to connect to simple FTP server with:")
			self.logger.log("[FtpConnector] IP "+self.ip+", port "+self.simplePort+", user "+self.user+", pwd "+self.pwd)
			ftp.connect(self.ip, self.simplePort, 10)
			self.logger.log("[FtpConnector] Logging in to FTP server")
			ftp.login(self.user, self.pwd)
			self.sendFilesSimple(ftp)
		except Exception as e:
			isConnected = False
			self.logger.logError("FtpConnector", "Error logging into simple ftp server, attempting to connect to simple backup FTP server", e)
		
		if isConnected:
			return
		
		try:
			#tries to connect to simple backup ftp server. Stops trying if this one is not successful
			self.logger.log("[FtpConnector] Attepting to connect to simple backup FTP server with:")
			self.logger.log("[FtpConnector] IP "+self.backupIp+", port "+self.simplePort+", user "+self.user+", pwd "+self.pwd)
			ftp.connect(self.backupIp, self.simplePort, 10)
			self.logger.log("[FtpConnector] Logging in to FTP server")
			ftp.login(self.user, self.pwd)
			self.sendFilesSimple(ftp)
		except Exception as e:
			self.logger.logError("FtpConnector", "Error logging into simple backup ftp server", e)
	
	#method checks if an ftp server is alive by sending it a pwd command
	#if an exception is thrown, the server is not alive
	def serverIsAlive(self, ftp):
		try:
			ftp.pwd()
		except Exception as e:
			self.logger.log("[FTPConnector] Server is no longer connected")
			return False
		return True
	
	#Backs up any FileOperations objects that we would like to send to the FTP server to the backup folder
	#if a data source is added to the program that records to a text file, ****ADD ITS BACKUP TO THIS METHOD****
	def backupTextFiles(self):
		self.logger.makeBackup(self.backupFolder, self.piName)
		self.recordingManager.temperatureReader.tempLogger.makeBackup(self.backupFolder, self.piName)
	
	#sends UDP message via the socket sock. If isBackup is true, sends it to the backup simple FTP Server ip address
	#otherwise, sends it to the normal server port
	def sendUDPMsg(self, msg, sock, isBackup=False):
		self.logger.log("[FTPConnector] Sending udp msg: " + msg)
		if isBackup:
			sock.sendto(str(msg), (self.backupIp, int(self.udpPort)))
		else:
			sock.sendto(str(msg), (self.ip, int(self.udpPort)))
	
	#sends alive requests to the FTP server on the UDP port (usually 8890 unless it is different in the config file)
	#used to let the advanced FTP know the pi is still responsive to requests
	def sendAliveMsg(self, sock):
		while self.sendAlive:
			self.logger.log("[FTPConnector] Sending alive msg")
			self.sendUDPMsg("alive " + self.piName, sock)
			time.sleep(5)
	
	#sends files to the ftpServer ftp. Uses udp communcation to wait until the server
	#tells it it is okay to send the files over
	def sendFilesAdvanced(self, ftp):
		self.archiveManager.stopArchiving()
		self.recordingManager.stopRecording()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(20)
		sock.bind(("", 0))
		#use udpReceiver to get messages from advanced FTP server
		udpReceiver = UDPReceiver(sock, self.logger)
		try:
			canConnect = False
			while not canConnect:
				#asking to start sending files
				self.sendUDPMsg("request_connect " + self.piName, sock)
				if not self.serverIsAlive(ftp):
					break
				time.sleep(5)
				msg = udpReceiver.getMsg().split(" ")
				if msg[0] != "":
					if len(msg) < 2:
						self.logger.log("[FTPConnector] received unrecognized message: " + str(msg))
					elif msg[0] == "connect" and msg[1] == self.piName:
						#response was we can start sending files
						self.logger.log("[FTPConnector] Ready to start transfer!")
						canConnect = True
						self.sendAlive = True
						#start sending alive requests because we are transferring now
						threading.Thread(target = self.sendAliveMsg, args = ([sock])).start()
					elif msg[0] == "no_connect" and msg[1] == self.piName:
						#response was we cannot send files yet
						self.logger.log("[FTPConnector] Not ready to transfer")
					else:
						self.logger.log("[FTPConnector] received unrecognized message: " + str(msg))
					
			if canConnect:
				#we have the goahead to send files now
				self.sendUDPMsg("message " + self.piName + " is starting to transfer data!", sock)
				#backup text files so we can send them over along with tar files
				#this is done right before transfer so we can send a relatively recent log file to the FTP server
				self.backupTextFiles()
				#gets the filenames of all the files in the backup folder
				filesToSend = self.getBackupFilenames()
				#these are used to tell the user of the FTP server how many files we have left to transfer
				count = 0
				total = len(filesToSend)
				#set the checkInterval to 900 seconds because we don't want to reconnect to the FTP server immidiately
				#after we are done sending data to it. It will be set back to 10 seconds if any errors occur in the transer
				self.checkInterval = 900
				for f in filesToSend:
					count += 1
					fullPath = os.path.join(self.backupFolder,f)
					try:
						if not self.serverIsAlive(ftp):
							#server must have disconnected!
							self.logger.log("[FTPConnector] Server unexpectedly disconnected, stopping transer")
							self.checkInterval = 10
							break
						#gets the size of the file we are about to send
						fileSizeMB = " ("+"{0:.2f}".format(float(os.path.getsize(fullPath))/(1024**2))+"MB)"
						#sends a message to the FTP server to let the user know what file we are transferring
						self.sendUDPMsg("message " + self.piName + " is sending file " + str(count) + " of " + str(total) + ": " + str(f) + fileSizeMB, sock)
						self.logger.log("[FtpConnector] Attempting to send file: " + fullPath)
						#attempt to send file
						ftp.storbinary("STOR " + f, open(fullPath, "rb"))
						self.logger.log("[FtpConnector] Successfully sent file: " + fullPath)
						subprocess.call(["sudo", "rm", fullPath])
						self.logger.log("[FtpConnector] Successfully deleted file: " + fullPath)
					except Exception as e:
						#something went wrong with a file transfer if we are here. We will still attempt to send the
						#rest of the files in out backup directory though
						self.checkInterval = 10
						self.logger.logError("FtpConnector", "Error with file transfer of " + fullPath, e)
				#send messages to let the ftp server know we are done transferring now
				self.sendUDPMsg("message " + self.piName + " is done transferring files", sock)
				self.sendUDPMsg("done " + self.piName, sock)
		except Exception as e:
			#if we end up here, something went wrong with the entire transfer. We do not attempt to send
			#any more files to this instance of the FTP connection
			self.checkInterval = 10
			self.logger.logError("FtpConnector", "Error with file transfer", e)
		#cleans up after sending files. Starts recording and archiving threads again, and stops keep alive messages
		self.sendAlive = False
		udpReceiver.stop()
		self.recordingManager.startRecording()
		self.archiveManager.startArchiving()
	
	#this performs almost the same as the AdvancedSendFiles
	#the main difference is that we send files without asking for permission from the FTP server via UDP
	#this means that multiple pi's could connect at once, slowing down network performance
	#udp messages are still sent to provide status updates to the user. If the user is running an FTP server
	#that does not have a UDP socket listener on self.udpPort, they will not receive the messages but this
	#will not impede file transferring
	def sendFilesSimple(self, ftp, isBackup=False):
		self.archiveManager.stopArchiving()
		self.recordingManager.stopRecording()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(20)
		sock.bind(("", 0))
		try:
			self.checkInterval = 900
			self.sendAlive = True
			self.sendUDPMsg("message " + self.piName + " is starting to transfer data!", sock, isBackup)
			#start sending alive requests because we are transferring now
			threading.Thread(target = self.sendAliveMsg, args = ([sock])).start()
			self.backupTextFiles()
			filesToSend = self.getBackupFilenames()
			count = 0
			total = len(filesToSend)
			for f in filesToSend:
				count += 1
				fullPath = os.path.join(self.backupFolder,f)
				try:
					if not self.serverIsAlive(ftp):
						self.checkInterval = 10
						self.logger.log("[FTPConnector] Server unexpectedly disconnected, stopping transer")
						break
					fileSizeMB = " ("+"{0:.2f}".format(float(os.path.getsize(fullPath))/(1024**2))+"MB)"
					self.sendUDPMsg("message " + self.piName + " is sending file " + str(count) + " of " + str(total) + ": " + str(f) + fileSizeMB, sock, isBackup)
					self.logger.log("[FtpConnector] Attempting to send file: " + fullPath)
					ftp.storbinary("STOR " + f, open(fullPath, "rb"))
					self.logger.log("[FtpConnector] Successfully sent file: " + fullPath)
					subprocess.call(["sudo", "rm", fullPath])
					self.logger.log("[FtpConnector] Successfully deleted file: " + fullPath)
				except Exception as e:
					self.checkInterval = 10
					self.logger.logError("FtpConnector", "Error with file transfer of " + fullPath, e)
			self.sendUDPMsg("message " + self.piName + " is done transferring files", sock, isBackup)
		except Exception as e:
			self.checkInterval = 10
			self.logger.logError("FtpConnector", "Error with file transfer", e)
		self.sendAlive = False
		self.recordingManager.startRecording()
		self.archiveManager.startArchiving()

	#gets the names of all the files in the backup directory
	def getBackupFilenames(self):
		return [f for f in os.listdir(self.backupFolder) if os.path.isfile(os.path.join(self.backupFolder, f))]
