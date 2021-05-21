#!/usr/bin/python

# --------------------------------------------
# Programma di esempio controllo stato GPIO17
#
# F.F. 03/05/2021
# --------------------------------------------

import os
import sys
import time

import RPi.GPIO as GPIO


SHUTDOWN_ENABLED = False	# Flag esecuzione shutdown

# Pulisce lo schermo
os.system("clear")

# Disattiva warnings GPIO
GPIO.setwarnings(False)

# Imposta modalita' utilizzo GPIO
GPIO.setmode(GPIO.BCM)

# Definisce la linee GPIO17 come ingresso
GPIO.setup(17, GPIO.IN) # GPIO17

print("Start GPIO test")
print("hit CTRL+C to exit")
print("-----------------------")
sys.stdout.flush()

make_shutdown = False

try:

	timectr=0
	while (not make_shutdown):
	
		print("Time: " + str(timectr) + "s")
		sys.stdout.flush()
		time.sleep(1)
		timectr = timectr + 1
		
		if (GPIO.input(17) == 1):
			print("RPIOFF: line activated, 60 seconds to shutdown!!")
			sys.stdout.flush()
			make_shutdown = True
		else:
			print("RPIOFF: line is not active - normal behavior")
			sys.stdout.flush()
			
	print("Shutdown mode activated!")
	sys.stdout.flush()
	# Comando di shutdown
	if (SHUTDOWN_ENABLED):
		subprocess.call(["shutdown", "-h", "now"])

except KeyboardInterrupt:
	print "Program termination detected!"
except SystemExit:
	print "System exit detected!"
except:
	print("Error detected!")
finally:
	print("Program exit.")
	sys.stdout.flush()
	sys.exit(0)
