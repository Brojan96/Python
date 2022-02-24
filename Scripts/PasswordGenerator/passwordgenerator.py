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
			
	while True:
		choice = input('Should the password contain uppercase characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ'
			break
		elif choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')

	while True: 
		choice = input('Should the password contain numbers? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '1234567890'
			break
		elif choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
			
	while True: 
		choice = input('Should the password contain special characters? [y]\n>').lower().strip()
		if choice in yes :
			characterlist = characterlist + '!"§$%&/()=?´`<>|@µ,.;:-_+*~ß?\}][{^°'
			break
		elif choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	password = ''.join(random.choices(characterlist, k=length))
	while True: 
		choice = input('Should the password be written into a text file? [n]\n>').lower().strip()
		if choice in yes :
			with open('password.txt', 'a') as f:
				f.write(password + '\n')
			break
		elif choice in no :
			break
		else :
			clearConsole()
			print('Please enter "yes" or "no"')
	print('\nGenerated Password:\n' + password + '\n')
			
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
passwordgenerator()