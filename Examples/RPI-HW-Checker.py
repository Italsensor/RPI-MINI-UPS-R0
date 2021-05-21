#!/usr/bin/python3
#
# Prerequisiti
# - Versione Python
# Richiesto Python3
#
# - Installazione pip3
# sudo apt-get install python3-pip
# sudo pip3 install setuptools
#
# - Installazione del package (globale)
#
# sudo pip3 install vcgencmd
# Per info: https://pypi.org/project/vcgencmd/
#
# - Esecuzione script
# python3 RPI-HW-Checker.py
#
# F.F. - 21/05/2021

import os
import sys
import time

from vcgencmd import Vcgencmd

if __name__ == "__main__":

	os.system("clear")

	vcgm = Vcgencmd()

	output = vcgm.version()
	print("Version: "+output)
	sys.stdout.flush()

	time.sleep(3)

	exitFlag = False	
	while not (exitFlag):
		try:
			
			os.system("clear")
			
			# Misura temperatura del SoC			
			output = vcgm.measure_temp()
			print("SoC temperature      : "+str(output))
			sys.stdout.flush()
			
			# Misura frequenza clock ARM
			output = vcgm.measure_clock("arm")
			print("ARM clock            : "+str(output))
			sys.stdout.flush()
			
			# Misura tensione del core
			output = vcgm.measure_volts("core")
			print("Core voltage         : "+str(output))
			sys.stdout.flush()
			
			# Misura allocazione memoria
			# Attenzione misura ARM non accurata, vedere info
			# su https://pypi.org/project/vcgencmd/
			output = vcgm.get_mem("arm")
			print("ARM memory allocation: "+str(output))
			sys.stdout.flush()
			output = vcgm.get_mem("gpu")
			print("GPU memory allocation: "+str(output))
			sys.stdout.flush()
			
			# Throttled state
			output_dict = vcgm.get_throttled()
			breakdown_dict = output_dict['breakdown']
			print("----------------------")
			print("Throttled state       ")
			print("----------------------")
			print(" Under-voltage detected             : "+str(breakdown_dict["0"]))
			print(" Arm frequency capped               : "+str(breakdown_dict["1"]))
			print(" Currently throttled                : "+str(breakdown_dict["2"]))
			print(" Soft temperature limit active      : "+str(breakdown_dict["3"]))
			print(" Under-voltage has occurred         : "+str(breakdown_dict["16"]))
			print(" Arm frequency capping has occurred : "+str(breakdown_dict["17"]))
			print(" Throttling has occurred            : "+str(breakdown_dict["18"]))
			print(" Soft temperature limit has occurred: "+str(breakdown_dict["19"]))
			sys.stdout.flush()
						
			time.sleep(1)
			
		except (KeyboardInterrupt, SystemExit) as ex:
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

	sys.exit(0)	