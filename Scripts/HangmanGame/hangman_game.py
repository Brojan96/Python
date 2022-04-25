import curses
from curses import wrapper
import random
import os
from time import sleep

#target = random.choice(wordlist.txt)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak() #optional, curses will react instantly, no need to press enter

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



def main(stdscr):
	curses.start_color()
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	stdscr.clear()
	for i in range(9):
		sleep(1)
		galgen(stdscr, i)
		stdscr.refresh()

	sleep(10)

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