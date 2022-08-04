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
4. Aufhübschen (programmieren) + Init anlegen
5. Ergebnis zeigen bei Verlust
6. Automatisches Zentrieren der Wörter und Sätze (semi-fertig, Gesuchtes Wort fehlt noch... ggf. noch die Zeilenhöhe zentrieren via curses.LINES // 2)
"""

f = open ("E:\\OneDrive\\Programming\\Python\\Scripts\\HangmanGame\\wordlist.txt", "r")

target_word = random.choice(f.read().splitlines()).upper()
guessed_letters = {}

stdscr = curses.initscr()
curses.start_color()

alphabet = list(string.ascii_uppercase)
for i in alphabet:
	guessed_letters[i] = curses.color_pair(3)

curses.noecho()

def galgen(stdscr, guesses):
	if (guesses>=1):
		stdscr.addstr(5, curses.COLS // 2 - 4, "/")
		stdscr.addstr(6, curses.COLS // 2 - 5, "/")
	if (guesses >= 2):
		stdscr.addstr(5, curses.COLS // 2 - 2, "\\")
		stdscr.addstr(6, curses.COLS // 2 - 1, "\\")
	if (guesses >= 3):
		stdscr.addstr(4, curses.COLS // 2 - 3, "|")
		stdscr.addstr(3, curses.COLS // 2 - 3, "|")
		stdscr.addstr(2, curses.COLS // 2 - 3, "|")
		stdscr.addstr(1, curses.COLS // 2 - 3, "|")
	if (guesses>=4):
		stdscr.addstr(0, curses.COLS // 2 - 2, "_")
		stdscr.addstr(0, curses.COLS // 2 - 1, "_")
		stdscr.addstr(0, curses.COLS // 2 - 0, "_")
		stdscr.addstr(0, curses.COLS // 2 + 1, "_")
		stdscr.addstr(0, curses.COLS // 2 + 2, "_")
	if (guesses>=5):
		stdscr.addstr(1, curses.COLS // 2 + 3, "|")
	if (guesses>=6):
		stdscr.addstr(2, curses.COLS // 2 + 3, "o")
	if (guesses>=7):
		stdscr.addstr(3, curses.COLS // 2 + 3, "|")
	if (guesses>=8):
		stdscr.addstr(4, curses.COLS // 2 + 2, "/")
		stdscr.addstr(4, curses.COLS // 2 + 4, "\\")
	if (guesses>=9):
		stdscr.addstr(2, curses.COLS // 2 + 2, "\\")
		stdscr.addstr(2, curses.COLS // 2 + 4, "/")

def alphabet():	
	stdscr.addstr(11, curses.COLS // 2 - 12, "A", guessed_letters["A"])
	stdscr.addstr(11, curses.COLS // 2 - 10, "B", guessed_letters["B"])
	stdscr.addstr(11, curses.COLS // 2 - 8, "C", guessed_letters["C"])
	stdscr.addstr(11, curses.COLS // 2 - 6, "D", guessed_letters["D"])
	stdscr.addstr(11, curses.COLS // 2 - 4, "E", guessed_letters["E"])
	stdscr.addstr(11, curses.COLS // 2 - 2, "F", guessed_letters["F"])
	stdscr.addstr(11, curses.COLS // 2 - 0, "G", guessed_letters["G"])
	stdscr.addstr(11, curses.COLS // 2 + 2, "H", guessed_letters["H"])
	stdscr.addstr(11, curses.COLS // 2 + 4, "I", guessed_letters["I"])
	stdscr.addstr(11, curses.COLS // 2 + 6, "J", guessed_letters["J"])
	stdscr.addstr(11, curses.COLS // 2 + 8, "K", guessed_letters["K"])
	stdscr.addstr(11, curses.COLS // 2 + 10, "L", guessed_letters["L"])
	stdscr.addstr(11, curses.COLS // 2 + 12, "M", guessed_letters["M"])
	stdscr.addstr(13, curses.COLS // 2 - 12, "N", guessed_letters["N"])
	stdscr.addstr(13, curses.COLS // 2 - 10, "O", guessed_letters["O"])
	stdscr.addstr(13, curses.COLS // 2 - 8, "P", guessed_letters["P"])
	stdscr.addstr(13, curses.COLS // 2 - 6, "Q", guessed_letters["Q"])
	stdscr.addstr(13, curses.COLS // 2 - 4, "R", guessed_letters["R"])
	stdscr.addstr(13, curses.COLS // 2 - 2, "S", guessed_letters["S"])
	stdscr.addstr(13, curses.COLS // 2 + 0, "T", guessed_letters["T"])
	stdscr.addstr(13, curses.COLS // 2 + 2, "U", guessed_letters["U"])
	stdscr.addstr(13, curses.COLS // 2 + 4, "V", guessed_letters["V"])
	stdscr.addstr(13, curses.COLS // 2 + 6, "W", guessed_letters["W"])
	stdscr.addstr(13, curses.COLS // 2 + 8, "X", guessed_letters["X"])
	stdscr.addstr(13, curses.COLS // 2 + 10, "Y", guessed_letters["Y"])
	stdscr.addstr(13, curses.COLS // 2 + 12, "Z", guessed_letters["Z"])

def targetWord(stdscr):
	finish = True

	for i,l in enumerate(target_word):
		L = l.upper()
		if guessed_letters[L] == curses.color_pair(1):
			stdscr.addstr(9, i, l, curses.color_pair(3)) #Daniel hilf mir, ohne das i zeigt er gar nichts an. :(

#curses.COLS // 2 - (len(target_word)// 2)

		else:
			stdscr.addstr(9, i, '_', curses.color_pair(3))
			finish = False

	return finish

def checkInput(stdscr, guesses):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	while True:
		key = stdscr.getkey().upper()
		if key not in alphabet:
			continue
		else:
			break

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
		stdscr.addstr(16, curses.COLS // 2 - len("You got away!") // 2, "You got away!", curses.color_pair(1))
		stdscr.refresh()

	else:
		galgen(stdscr, guesses)
		alphabet()
		targetWord(stdscr)
		stdscr.addstr(16, curses.COLS // 2 - len("You are dead, boi!") // 2, "You are dead, boi!", curses.color_pair(2))
		stdscr.refresh()
	stdscr.getkey()

if __name__=="__main__":
	wrapper(main)