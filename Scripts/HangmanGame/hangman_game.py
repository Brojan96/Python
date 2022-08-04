import curses
from curses import wrapper
import random
from time import sleep
from turtle import color
import string

"""
TODO: 
1. User Input + Graphische Darstellung
2. Spielregeln festlegen
3. Wordlist erweitern
4. Aufhübschen + Init anlegen
"""

f = open ("E:\\OneDrive\\Programming\\Python\\Scripts\\HangmanGame\\wordlist.txt", "r")

target_word = random.choice(f.read().splitlines()).upper()
#target_word = target_word.upper
guessed_letters = {}

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
	stdscr.addstr(11, 1, "A", guessed_letters["A"])
	stdscr.addstr(11, 3, "B", guessed_letters["B"])
	stdscr.addstr(11, 5, "C", guessed_letters["C"])
	stdscr.addstr(11, 7, "D", guessed_letters["D"])
	stdscr.addstr(11, 9, "E", guessed_letters["E"])
	stdscr.addstr(11, 11, "F", guessed_letters["F"])
	stdscr.addstr(11, 13, "G", guessed_letters["G"])
	stdscr.addstr(11, 15, "H", guessed_letters["H"])
	stdscr.addstr(11, 17, "I", guessed_letters["I"])
	stdscr.addstr(11, 19, "J", guessed_letters["J"])
	stdscr.addstr(11, 21, "K", guessed_letters["K"])
	stdscr.addstr(11, 23, "L", guessed_letters["L"])
	stdscr.addstr(11, 25, "M", guessed_letters["M"])
	stdscr.addstr(13, 1, "N", guessed_letters["N"])
	stdscr.addstr(13, 3, "O", guessed_letters["O"])
	stdscr.addstr(13, 5, "P", guessed_letters["P"])
	stdscr.addstr(13, 7, "Q", guessed_letters["Q"])
	stdscr.addstr(13, 9, "R", guessed_letters["R"])
	stdscr.addstr(13, 11, "S", guessed_letters["S"])
	stdscr.addstr(13, 13, "T", guessed_letters["T"])
	stdscr.addstr(13, 15, "U", guessed_letters["U"])
	stdscr.addstr(13, 17, "V", guessed_letters["V"])
	stdscr.addstr(13, 19, "W", guessed_letters["W"])
	stdscr.addstr(13, 21, "X", guessed_letters["X"])
	stdscr.addstr(13, 23, "Y", guessed_letters["Y"])
	stdscr.addstr(13, 25, "Z", guessed_letters["Z"])

def targetWord(stdscr):
	finish = True

	for i,l in enumerate(target_word):
		L = l.upper()
		if guessed_letters[L] == curses.color_pair(1):
			stdscr.addstr(9, 8+i, l, curses.color_pair(3))
		else:
			stdscr.addstr(9, 8+i, '_', curses.color_pair(3))
			finish = False
	return finish

# FUNKTION die checkt, ob der Input korrekt ist. falls ja: grünen colorcode hinterlegen, falls nein: roten hinterlegen
# Funktion, die das Lösungswort in unterstrichen darstellt, solange diese noch nicht korrekt geraten wurden. 
# Wenn sie dann richtig geraten werden, erscheinen die Buchstaben.

def checkInput(stdscr, guesses):
	key = stdscr.getkey().upper()

	if key not in target_word:
		if guessed_letters[key] != curses.color_pair(2):
			guessed_letters[key] = curses.color_pair(2)
			return guesses + 1
		else:
			return guesses

	else:
		guessed_letters[key] = curses.color_pair(1)
		return guesses

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	guesses = 0
	Victory = False

	stdscr.clear()
	alphabet()
	targetWord(stdscr)
	stdscr.refresh()
	
	while guesses < 9 :
		galgen(stdscr, guesses)
		guesses = checkInput(stdscr, guesses)
		alphabet()
		Victory = targetWord(stdscr)
		stdscr.refresh()
		if Victory:
			break
	
	if Victory:
		galgen(stdscr, guesses)
		alphabet()
		targetWord(stdscr)
		stdscr.addstr(16, 5, "You got away!", curses.color_pair(1))
		stdscr.refresh()
	else:
		galgen(stdscr, guesses)
		alphabet()
		targetWord(stdscr)
		stdscr.addstr(16, 5, "You are dead, boi!", curses.color_pair(2))
		stdscr.refresh()
	stdscr.getkey()

if __name__=="__main__":
	wrapper(main)