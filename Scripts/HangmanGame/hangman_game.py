import curses
from curses import wrapper
import random
import os
from time import sleep
from turtle import color
import string

#target = random.choice(wordlist.txt)
guessed_letters = {}
amount_of_guesses = 0

stdscr = curses.initscr()
curses.start_color()


alphabet = list(string.ascii_uppercase)
for i in alphabet:
	guessed_letters[i] = curses.color_pair(3)

#stdscr.addstr (str(guessed_letters))
#stdscr.refresh()
#sleep (60)


curses.noecho()
#curses.cbreak() #optional, curses will react instantly, no need to press enter

def galgen(stdscr, guesses):
	if (guesses>=1):
		stdscr.addstr(5, 1, "/")
		stdscr.addstr(6, 0, "/")
	if (guesses >= 2):
		stdscr.addstr(5, 3, "\\")
		stdscr.addstr(6, 4, "\\")
	if (guesses >= 3):
		stdscr.addstr(4, 2, "|")
		stdscr.addstr(3, 2, "|")
		stdscr.addstr(2, 2, "|")
		stdscr.addstr(1, 2, "|")
	if (guesses>=4):
		stdscr.addstr(0, 3, "_")
		stdscr.addstr(0, 4, "_")
		stdscr.addstr(0, 5, "_")
		stdscr.addstr(0, 6, "_")
		stdscr.addstr(0, 7, "_")
	if (guesses>=5):
		stdscr.addstr(1, 8, "|")
	if (guesses>=6):
		stdscr.addstr(2, 8, "o")
	if (guesses>=7):
		stdscr.addstr(3, 8, "|")
	if (guesses>=8):
		stdscr.addstr(4, 7, "/")
		stdscr.addstr(4, 9, "\\")
	if (guesses>=9):
		stdscr.addstr(2, 7, "\\")
		stdscr.addstr(2, 9, "/")

def alphabet():	
	stdscr.addstr(9, 1, "A", guessed_letters["A"])
	stdscr.addstr(9, 3, "B", guessed_letters["B"])
	stdscr.addstr(9, 5, "C", guessed_letters["C"])
	stdscr.addstr(9, 7, "D", guessed_letters["D"])
	stdscr.addstr(9, 9, "E", guessed_letters["E"])
	stdscr.addstr(9, 11, "F", guessed_letters["F"])
	stdscr.addstr(9, 13, "G", guessed_letters["G"])
	stdscr.addstr(9, 15, "H", guessed_letters["H"])
	stdscr.addstr(9, 17, "I", guessed_letters["I"])
	stdscr.addstr(9, 19, "J", guessed_letters["J"])
	stdscr.addstr(9, 21, "K", guessed_letters["K"])
	stdscr.addstr(9, 23, "L", guessed_letters["L"])
	stdscr.addstr(9, 25, "M", guessed_letters["M"])
	stdscr.addstr(11, 1, "N", guessed_letters["N"])
	stdscr.addstr(11, 3, "O", guessed_letters["O"])
	stdscr.addstr(11, 5, "P", guessed_letters["P"])
	stdscr.addstr(11, 7, "Q", guessed_letters["Q"])
	stdscr.addstr(11, 9, "R", guessed_letters["R"])
	stdscr.addstr(11, 11, "S", guessed_letters["S"])
	stdscr.addstr(11, 13, "T", guessed_letters["T"])
	stdscr.addstr(11, 15, "U", guessed_letters["U"])
	stdscr.addstr(11, 17, "V", guessed_letters["V"])
	stdscr.addstr(11, 19, "W", guessed_letters["W"])
	stdscr.addstr(11, 21, "X", guessed_letters["X"])
	stdscr.addstr(11, 23, "Y", guessed_letters["Y"])
	stdscr.addstr(11, 25, "Z", guessed_letters["Z"])
	stdscr.refresh()

# FUNKTION die checkt, ob der Input korrekt ist. falls ja: grünen colorcode hinterlegen, falls nein: roten hinterlegen
# Funktion, die das Lösungswort in unterstrichen darstellt, solange diese noch nicht korrekt geraten wurden. 
# Wenn sie dann richtig geraten werden, erscheinen die Buchstaben.


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	stdscr.clear()
	alphabet()
	for i in range(10):
		sleep(1)
		galgen(stdscr, i)
		stdscr.refresh()

	sleep(60)

	"""
	while guesses < 11:
		try:
			key = stdscr.getkey()

			if key in target
				stdscr.addstr(key, 1, 0)
			else :
				print(Galgen)

        except:
            continue

		
"""

if __name__=="__main__":
	wrapper(main)