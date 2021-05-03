#!/usr/bin/python
#
# Utilizzo di subprocess per eseguire comandi
# come se si fosse nella shell e recuperandone
# l'output

import os
import sys
import subprocess

# -------------------------------------------------------------
#                             MAIN
# -------------------------------------------------------------
if __name__ == "__main__":

	# Pulisce lo schermo
	os.system("clear")
	sys.stdout.flush()

	try:
	
		# Visualizza il comando
		print("Command     : i2cget -y 1 0x08 0x00 b")
		sys.stdout.flush()

		# Formatta il comando per essere utilizzato con Popen.
		# Il primo argomento e' il comando da eseguire,
		# i restanti elementi sono gli argomenti che saranno
		# passati al comando
		cmd = ["i2cget", "-y", "1", "0x08", "0x00", "b"]
		# Apre il processo
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		# Interagisce con il processo
		out, err = p.communicate()
		# Visualizza il valore restituito dal processo
		print ("Readed value:" + out)
		sys.stdout.flush()
		
	except Exception as ex:
		# Gestione qualsiasi altra eccezione
		template =  "ERROR: An exception of type {0} occured." + \
				    "Arguments:\n{1!r}"
		msg = template.format(type(ex).__name__, ex.args)
		print(msg)
		sys.stdout.flush()
	finally:
		# Codice di uscita
		print("(main) Exiting from main program")
		sys.stdout.flush()
		sys.exit(0)
