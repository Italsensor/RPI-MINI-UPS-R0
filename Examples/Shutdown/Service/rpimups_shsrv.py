#!/usr/bin/python

# ----------------------------------------------------
# Servizio gestione shutdown da linea RPIOFF
#
# F.F. 03/05/2021
# ----------------------------------------------------

import RPi.GPIO as GPIO
import time
import os
import sys
from datetime import datetime
import subprocess

# Determina la data corrente
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

# Definisce file Log in modalita append, e flush immediato
LogFilename = "/home/pi/rpimups_shsrv.log"
logFile = open(LogFilename, 'a', 0)
logFile.write('rpimups_shsrv started on: ' + date_time + '\n')

# Disattiva warnings GPIO
GPIO.setwarnings(False)

# Imposta modalita' utilizzo GPIO
GPIO.setmode(GPIO.BCM)

# Definisce le linee GPIO
GPIO.setup(17, GPIO.IN) # GPIO17 input (RPIOFF)

flag = False
try:
	while (True):
		# GPIO17: gestione ingresso RPIOFF per shutdown
		if (GPIO.input(17) == 1):
			# Attende 5 secondi dopo che la linea
			# RPIOFF e' stata attivata
			counter = 5
			time.sleep(1)
			GPIO.cleanup()
			# Scrive sul Log
			now = datetime.now()
			date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
			logFile.write('rpimups_shsrv fire shutdown on: ' + date_time + '\n')
			logFile.close()
			time.sleep(0.5)
			# Comando di shutdown
			subprocess.call(["shutdown", "-h", "now"])
			break
except Exception as ex:
	print('Exception detect!')
	sys.stdout.flush()
	template = "An exception of type {0} occurred. Arguments:\n{1!r}"
	message = template.format(type(ex).__name__, ex.args)
	print(message)
	sys.stdout.flush()
finally:
	sys.exit(0)

