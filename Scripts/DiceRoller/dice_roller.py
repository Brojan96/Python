import random
import os
global values
values = []

def numberandpositive(x, standardvalue):
	while True:
		try: #validate that the input is numeric and positive
			if x == '':
				x = standardvalue
			y = int(x)
			if y < 1:
				clearConsole()
				x=input(f'Please enter a positive number. [{standardvalue}]\n>')
				continue
			values.append(y)
			break
		except:
			clearConsole()
			x=input(f'Please enter a numeric value or press enter to set the standard value [{standardvalue}].\n>')

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)

def dice_roller() :
	clearConsole()
	x = input('How many dices should I roll for you? [1]\n>')
	numberandpositive(x, 1)
	clearConsole()
	x = input('Lowest possible number? [1]\n>')
	numberandpositive(x, 1)
	clearConsole()
	x = input('Highest possible number? [6]\n>')
	numberandpositive(x, 6)
	clearConsole()
	counter = 0
	while counter < values[0] :
		counter = counter + 1
		result = random.randint(values[1], values[2])
		print(result)
if __name__=="__main__":
	dice_roller()