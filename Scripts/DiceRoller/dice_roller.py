import random
import os

def dice_roller() :
	clearConsole()
	while True:
		low_end = input('Lowest possible number? [1]')
		try: #validate that the input is numeric and positive
			if low_end == '' :
				low_end = int(1)
			low_end = int(low_end)
			if low_end < 1:
				clearConsole()
				print('Please enter a positive number.\n')
				continue
			break
		except:
			clearConsole()
			print('Please enter a numeric value :(\n')
	while True:
		high_end = input('Highest possible number? [6]')
		try: #validate that the input is numeric and positive
			if high_end == '' :
				high_end = int(6)
			high_end = int(high_end)
			if high_end < 1:
				clearConsole()
				print('Please enter a positive number.\n')
				continue
			break
		except:
			clearConsole()
			print('Please enter a numeric value :(\n')
	result = int(random.uniform(low_end, high_end))
	print(result)
def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)
dice_roller()