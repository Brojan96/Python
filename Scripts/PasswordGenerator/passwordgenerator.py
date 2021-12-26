import random
import os

def passwordgenerator() :
	clearConsole()
	yes = set(['yes','y', 'ye', ''])
	no = set(['no','n', 'ne'])
	characterlist = 'abcdefghijklmnopqrstuvwxyzäöü'
	while True :
		length = input('How many characters should your password be? [50]\n>')
		try:
			if length == '' :
				length = int(50)
			length = int(length)
			if length < 1:
				clearConsole()
				print('Please enter a positive number.\n')
				continue
			break
		except:
			clearConsole()
			print('Please enter a numeric value :(\n')
		#if length == '' : 
		#	length = int(50)
		#	break
		#elif (length < 1) :
			
	while True:
		choice = input('Should the password contain uppercase characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ'
			break
		if choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	while True: 
		choice = input('Should the password contain numbers? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '1234567890'
			break
		if choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	while True: 
		choice = input('Should the password contain special characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '!"§$%&/()=?´`<>|@µ,.;:-_+*~ß?\}][{^°'
			break
		if choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	password = ''.join(random.choices(characterlist, k=length))
	print('\nGenerated Password:\n' + password + '\n')
			
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
passwordgenerator()