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
			print('Please enter a numeric value :(\n')

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)

def dice_roller() :
	clearConsole()
	x = input('How many dices should I roll for you? [1]')
	numberandpositive(x, 1)
	clearConsole()
	x = input('Lowest possible number? [1]')
	numberandpositive(x, 1)
	clearConsole()
	x = input('Highest possible number? [6]')
	numberandpositive(x, 6)
	clearConsole()
	counter = 0
	while counter < int(values[0]) :
		counter = counter + 1
		result = int(random.uniform(int(values[1]), int(values[2])))
		print(result)
dice_roller()