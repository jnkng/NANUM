# Program : nmconsole.py
# Developer : Cat|less
# Python 3.7.3

# Basic UI Functions
def banner():
	banner_context = """
NANUM CONSOLE v0.1
       by Cat|less
	"""
	return banner_context
def help():
	help_context = """
Basic Commands
===============

Command\t\t\tDescription
-------\t\t\t-----------
?      \t\t\tHelp Menu
banner \t\t\tDisplay a NANUM Main Banner


	"""
	return help_context

# Module Control Functions
def status():
	stat_context = """
 [*] NANUM STATUS SCREEN
   [+] ACTIVE
""" + "      Modules" + """
   [-] INACTIVE 
""" + "      Modules\n"
	return stat_context[1:]

# Sub Funstions
def getStat():
	pass

#################
# Main Function #
#################

if __name__ == "__main__":
	# Printing Banner
	print(banner())

	# Command Control
	cmd = ""
	while cmd not in ["q","quit","exit"]:
		cmd = raw_input("nmconsole > ")
		cmd = cmd.lower().strip()

		if cmd in ["?","help","h"]:
			print(help())
		elif cmd in ["banner"]:
			print(banner())
		elif cmd in ["status","stat"]:
			print(status())		
		elif cmd in ["control"]:
			pass		
		elif cmd in [""]:
			pass		
		elif cmd in [""]:
			pass		
		elif cmd in [""]:
			pass	
			
	


