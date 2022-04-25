import curses
from curses import wrapper
import random
import os

target = random.choice(wordlist.txt)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak() #optional, curses will react instantly, no need to press enter

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	stdscr.clear()
	while guesses < 11:
		try:
			key = stdscr.getkey()

			if key in target
				stdscr.addstr(key, 1, 0)
			else :
				print(Galgen)

        except:
            continue

		
		

def hangman_game() :
	global answer
	global hangman_word
	global guessed_letters
	global guesses
	wordlist = open("wordlist.txt", "rt")
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		wordlist = open("wordlist.txt", "rt").strip()
	guesses = 0
	guessed_letters = None
	hangman_word=','.join(random.choices(wordlist))
	while guesses < 10 :
		answer = input('Guess a letter :)\n').lower().strip()
		if answer == 'clear' :
			clearConsole()
			continue
		elif answer == '' :
			print('Please enter an alphabetical value.\n')
			continue
		elif len(answer) > 1:
			print('Please enter only one letter.\n')
			continue
		elif str.isalpha(answer) == False :
			print('Please enter an alphabetical value.\n')
			continue
		else :
			game_engine()

def game_engine() :
	clearConsole()
	if guessed_letters == hangman_word :
		guessed_letters = guessed_letters + answer
		guesses = guesses + 1
		print(guessed_letters)
	elif guessed_letters != hangman_word :
		guesses = guesses + 1

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)
hangman_game()
