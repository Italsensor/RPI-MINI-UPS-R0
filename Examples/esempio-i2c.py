#!/usr/bin/python
# --------------------------------------------------
# Prerequisiti
# sudo apt-get install python-smbus python-dev
#
# Determinare numero bus I2C
# ls -l /dev/i2c-1
# crw-rw---- 1 root i2c 89, 1 Feb 14  2019 /dev/i2c-1
# --------------------------------------------------

import os
import sys
import smbus	# Per gestione bus I2C
import time

UP_DEVICE_ADDRESS = 0x08	# Indirizzo microcontrollore
UP_REG_ADDRESS = 0x00		# Registro microcontrollore

# -------------------------------------------------------------
#                             MAIN
# -------------------------------------------------------------
if __name__ == "__main__":
	
	# Pulisce lo schermo
	os.system("clear")
	
	# BUS I2C-1 (vedere risposta al comando ls -l /dev/i2c-1)
	rpi_bus = smbus.SMBus(1)

	cycle_counter = 0
	while True:
		
		try:
			cycle_counter=+1;
			
			print("--------------------------------------------------")
			sys.stdout.flush()
			print("Ciclo lettura-incremento-scrittura-lettura numero: " \
				  +str(cycle_counter))
			sys.stdout.flush()
			print("Premere CTR+C per uscire.")
			sys.stdout.flush()
			print("--------------------------------------------------")
			sys.stdout.flush()
			
			# Esegue la lettura del registro specificato
			byte_val = rpi_bus.read_byte_data(UP_DEVICE_ADDRESS, UP_REG_ADDRESS)
			print(  "Lettura registro  : " + str(UP_REG_ADDRESS) + \
					" - Valore letto: " + str(byte_val))
			sys.stdout.flush()
			
			time.sleep(1)
			
			# Incremento di 1 il valore del dato letto
			byte_val += 1
			print("Incremento il valore letto di 1")
			sys.stdout.flush()
			
			# Esegue una scrittura singola sul registro specificato
			print(  "Scrittura Registro: " + str(UP_REG_ADDRESS) + \
					" - Valore scritto: " + str(byte_val))
			sys.stdout.flush()
			rpi_bus.write_byte_data(UP_DEVICE_ADDRESS, UP_REG_ADDRESS, byte_val)
			
			time.sleep(1)
			
			# Esegue una nuova lettura dello stesso registro
			byte_val = rpi_bus.read_byte_data(UP_DEVICE_ADDRESS,UP_REG_ADDRESS)
			print(  "Lettura registro  : " + str(UP_REG_ADDRESS) + \
					" - Valore letto: " + str(byte_val))
			sys.stdout.flush()
			
			# Pausa prima del prossimo ciclo
			time.sleep(5)
			
		except (KeyboardInterrupt, SystemExit), ex:
			# Gestisce interruzione CTRL+C
			print("CTRL-C detected!")
			sys.stdout.flush()
			sys.exit(0)
		except Exception as ex:
			# Gestione qualsiasi altra eccezione
			template =  "ERROR: An exception of type {0} occured." + \
						"Arguments:\n{1!r}"
			msg = template.format(type(ex).__name__, ex.args)
			print(msg)
			sys.stdout.flush()
			# Codice di uscita
			print("(main) Exiting from main program")
			sys.stdout.flush()
			sys.exit(0)

			
