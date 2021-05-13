#!/usr/bin/python
# --------------------------------------------------
# Prerequisiti:
#
# sudo apt-get install python-serial
# sudo apt-get install python3-serial
# sudo apt-get install python3-serial-asyncio
# --------------------------------------------------

import sys
import time
import threading
import serial

exitFlag = False

# ----------------------------------------------------------------
# Thread di ricezione dati porta seriale
# ----------------------------------------------------------------
class rcvSerialThread(threading.Thread):
	def __init__(self, serialPortObj, threadID, threadname, pollingTime):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadname = threadname
		self.pollingTime= pollingTime
		self.serialPortObj = serialPortObj
		self.rxByte = 0
		self.buffer = ""
		self.bFlagRx = False

	def run(self):
		print("Starting " + self.threadname)

		while not(exitFlag):
			#time.sleep(self.pollingTime)
			intNoChars = self.serialPortObj.inWaiting()
			if (intNoChars > 0):
				self.rxByte = self.serialPortObj.read(1)
				if (self.rxByte == "$"):
					self.buffer = "$"
				elif ( (self.rxByte <> "!") and (self.rxByte <> "%") ):
					self.buffer = self.buffer + self.rxByte
				elif ( (self.rxByte == "!") or (self.rxByte == "%") ):
					self.buffer = self.buffer + self.rxByte
					print("RX <= " + (self.buffer))
					self.bFlagRx=True

		print("Exiting " + self.threadname)
		return
	
	def readBuffer(self, rxbuffer):
		msg=""
		if (self.bFlagRx):
			msg = self.buffer
			self.buffer = ""
		else:
			msg = ""
		return (msg)

# ----------------------------------------------------------------	
# Wrapper per porta seriale con gestione attraverso Thread
# ----------------------------------------------------------------
class gestSerialPort (serial.Serial):
	def __init__(self, *args, **kwargs):
		serial.Serial.__init__(self, *args, **kwargs)
		self.rxbuffer = ""
	
	def setupPollingTime(self, pollingTime):
		# Setup the polling time for the thread
		self.pollingTime = pollingTime

	def startPollingThread(self):
		# Setup and start of the rcv thread
		self.rcvEventTh = rcvSerialThread(self,1,"RXThread", self.pollingTime)
		self.rcvEventTh.start()
	
 	def writeSerial(self, buffer):
		self.write(buffer)

	def readRxBuffer(self):
		return(self.rcvEventTh.readBuffer(self.rxbuffer))

# ================================================================
# main code
# ================================================================

# -------------------------------------------------------------
#                             MAIN
# -------------------------------------------------------------
if __name__ == "__main__":

	strInputBuffer = ""

	# Crea la porta seriale ed esegue il thread di ricezione
	mySerialPort = gestSerialPort("/dev/ttyAMA0", 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
	mySerialPort.setupPollingTime(0.5)	# Non utilizzato
	mySerialPort.startPollingThread()

	time.sleep(1)

	# Messaggio porta seriale operativa
	mySerialPort.writeSerial("Serial port running...")

	while not (exitFlag):
		
		try:

			# Ciclo attesa utente
			strInputBuffer = raw_input("TX => ")
			mySerialPort.writeSerial(str(strInputBuffer))
				
		except (KeyboardInterrupt, SystemExit), ex:
			# Gestisce interruzione CTRL+C
			print("CTRL-C detected!")
			sys.stdout.flush()
			exitFlag = True
		except Exception as ex:
			# Gestione qualsiasi altra eccezione
			template =  "ERROR: An exception of type {0} occured." + \
						"Arguments:\n{1!r}"
			msg = template.format(type(ex).__name__, ex.args)
			print(msg)
			sys.stdout.flush()
			exitFlag = True
		
	# Stop all threads and exit
	exitFlag = True
	# Codice di uscita
	print("(main) Exiting from main program")
	sys.stdout.flush()
	sys.exit(0)
