import threading

#simple class that tries to get messages from socket sock until it is told to stop
#by calling stop()
#other threads can get messages it might have recieved by calling .getMsg()
class UDPReceiver:
	def __init__(self, sock, logger):
		self.msgQueue = Queue.Queue()
		self.send = True
		self.sock = sock
		self.receiveThread = threading.Thread(target = self.receiveLoop, args = ())
		self.receiveThread.start()
		self.logger = logger
		
	def receiveLoop(self):
		while True:
			try:
				if self.send == False:
					return
				data, addr = self.sock.recvfrom(1024)
				self.logger.log("[UDPReceiver] received message: " + str(data))
				self.msgQueue.put(str(data))
			except socket.timeout as e:
				if self.send == False:
					return
				self.logger.log("[UDPReceiver] socket timed out")
	def getMsg(self):
		if self.msgQueue.empty():
			return ""
		else:
			return str(self.msgQueue.get_nowait())
	def stop(self):
		self.logger.log("[UDPReceiver] stopping receiving")
		self.send = False
