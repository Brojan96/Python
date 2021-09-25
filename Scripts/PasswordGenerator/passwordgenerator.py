import random
import os

#yes = set(['yes','y', 'ye', ''])
#no = set(['no','n'])
#choice = raw_input(answer).lower()

def passwordgenerator() :
	clearConsole()
	yes = set(['yes','y', 'ye', ''])
	characterlist = 'abcdefghijklmnopqrstuvwxyzäöü'
	while True :
		length = input('How many characters should your password be? [50]\n>') 
		if length == '' : 
			length = int(50)
			break
		else :
			try:
				length = int (length)
				break
			except:
				clearConsole()
				print('Please enter a number :(')
	while True:
		choice = input('Should the password contain uppercase characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ'
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	while True: 
		choice = input('Should the password contain numbers? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '1234567890'
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	while True: 
		choice = input('Should the password contain special characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '!"§$%&/()=?´`<>|@µ,.;:-_+*~ß?\}][{^°'
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	password = ''.join(random.sample(characterlist, length))
	print('\nGenerated Password:\n' + password)
			
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
passwordgenerator()

