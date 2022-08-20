import curses
import string

class Hangman:
	def __init__(self, targetWord):
		self.targetWord = targetWord
		self.guessedLetters = {}

		self.stdscr = curses.initscr()
		curses.start_color()
		curses.noecho()

		self.alphabet = list(string.ascii_uppercase)
		for i in self.alphabet:
			self.guessedLetters[i] = curses.color_pair(3)
		
		self.guesses = 0

	def galgen(self):
		while True:
			try:	
				if (self.guesses >= 1):
					self.stdscr.addstr(5, curses.COLS // 2 - 4, "/")
					self.stdscr.addstr(6, curses.COLS // 2 - 5, "/")
				if (self.guesses >= 2):
					self.stdscr.addstr(5, curses.COLS // 2 - 2, "\\")
					self.stdscr.addstr(6, curses.COLS // 2 - 1, "\\")
				if (self.guesses >= 3):
					self.stdscr.addstr(4, curses.COLS // 2 - 3, "|")
					self.stdscr.addstr(3, curses.COLS // 2 - 3, "|")
					self.stdscr.addstr(2, curses.COLS // 2 - 3, "|")
					self.stdscr.addstr(1, curses.COLS // 2 - 3, "|")
				if (self.guesses>=4):
					self.stdscr.addstr(0, curses.COLS // 2 - 2, "_")
					self.stdscr.addstr(0, curses.COLS // 2 - 1, "_")
					self.stdscr.addstr(0, curses.COLS // 2 - 0, "_")
					self.stdscr.addstr(0, curses.COLS // 2 + 1, "_")
					self.stdscr.addstr(0, curses.COLS // 2 + 2, "_")
				if (self.guesses>=5):
					self.stdscr.addstr(1, curses.COLS // 2 + 3, "|")
				if (self.guesses>=6):
					self.stdscr.addstr(2, curses.COLS // 2 + 3, "o")
				if (self.guesses>=7):
					self.stdscr.addstr(3, curses.COLS // 2 + 3, "|")
				if (self.guesses>=8):
					self.stdscr.addstr(4, curses.COLS // 2 + 2, "/")
					self.stdscr.addstr(4, curses.COLS // 2 + 4, "\\")
				if (self.guesses>=9):
					self.stdscr.addstr(2, curses.COLS // 2 + 2, "\\")
					self.stdscr.addstr(2, curses.COLS // 2 + 4, "/")
				break
			except curses.error:
				self.stdscr.erase()
				self.stdscr.addstr(0, 0, "Error, the console is too small. Please enlarge it to atleast 25 lines and columns and press a key afterwards.", curses.color_pair(3))
				self.stdscr.refresh()
				self.stdscr.getkey()
				self.stdscr.erase()
	
	def diplayAlphabet(self):
		while True:
			try:
				self.stdscr.addstr(13, curses.COLS // 2 - 12, "A", self.guessedLetters["A"])
				self.stdscr.addstr(13, curses.COLS // 2 - 10, "B", self.guessedLetters["B"])
				self.stdscr.addstr(13, curses.COLS // 2 - 8, "C", self.guessedLetters["C"])
				self.stdscr.addstr(13, curses.COLS // 2 - 6, "D", self.guessedLetters["D"])
				self.stdscr.addstr(13, curses.COLS // 2 - 4, "E", self.guessedLetters["E"])
				self.stdscr.addstr(13, curses.COLS // 2 - 2, "F", self.guessedLetters["F"])
				self.stdscr.addstr(13, curses.COLS // 2 - 0, "G", self.guessedLetters["G"])
				self.stdscr.addstr(13, curses.COLS // 2 + 2, "H", self.guessedLetters["H"])
				self.stdscr.addstr(13, curses.COLS // 2 + 4, "I", self.guessedLetters["I"])
				self.stdscr.addstr(13, curses.COLS // 2 + 6, "J", self.guessedLetters["J"])
				self.stdscr.addstr(13, curses.COLS // 2 + 8, "K", self.guessedLetters["K"])
				self.stdscr.addstr(13, curses.COLS // 2 + 10, "L", self.guessedLetters["L"])
				self.stdscr.addstr(13, curses.COLS // 2 + 12, "M", self.guessedLetters["M"])
				self.stdscr.addstr(15, curses.COLS // 2 - 12, "N", self.guessedLetters["N"])
				self.stdscr.addstr(15, curses.COLS // 2 - 10, "O", self.guessedLetters["O"])
				self.stdscr.addstr(15, curses.COLS // 2 - 8, "P", self.guessedLetters["P"])
				self.stdscr.addstr(15, curses.COLS // 2 - 6, "Q", self.guessedLetters["Q"])
				self.stdscr.addstr(15, curses.COLS // 2 - 4, "R", self.guessedLetters["R"])
				self.stdscr.addstr(15, curses.COLS // 2 - 2, "S", self.guessedLetters["S"])
				self.stdscr.addstr(15, curses.COLS // 2 + 0, "T", self.guessedLetters["T"])
				self.stdscr.addstr(15, curses.COLS // 2 + 2, "U", self.guessedLetters["U"])
				self.stdscr.addstr(15, curses.COLS // 2 + 4, "V", self.guessedLetters["V"])
				self.stdscr.addstr(15, curses.COLS // 2 + 6, "W", self.guessedLetters["W"])
				self.stdscr.addstr(15, curses.COLS // 2 + 8, "X", self.guessedLetters["X"])
				self.stdscr.addstr(15, curses.COLS // 2 + 10, "Y", self.guessedLetters["Y"])
				self.stdscr.addstr(15, curses.COLS // 2 + 12, "Z", self.guessedLetters["Z"])
				break
			
			except curses.error:
				self.stdscr.erase()
				self.stdscr.addstr(0, 0, "Error, the console is too small. Please enlarge it to atleast 25 lines and columns and press a key afterwards.", curses.color_pair(3))
				self.stdscr.refresh()
				self.stdscr.getkey()
				self.stdscr.erase()	

	def diplayTargetWord(self, gameover):
		finish = True

		if gameover == "Win":
			self.stdscr.addstr(9, curses.COLS // 2 - (len(self.targetWord) // 2), self.targetWord, curses.color_pair(1))
			return finish

		elif gameover == "Lose":
			for i,l in enumerate(self.targetWord):
				L = l.upper()
				if self.guessedLetters[L] == curses.color_pair(1):
					self.stdscr.addstr(9, curses.COLS // 2 - (len(self.targetWord) // 2) + i, l, curses.color_pair(3))
				else:
					self.stdscr.addstr(9, curses.COLS // 2 - (len(self.targetWord) // 2) + i, l, curses.A_UNDERLINE + curses.color_pair(2))
			return finish

		for i,l in enumerate(self.targetWord):
			L = l.upper()
			if self.guessedLetters[L] == curses.color_pair(1):
				self.stdscr.addstr(9, curses.COLS // 2 - (len(self.targetWord) // 2) + i, l, curses.color_pair(3))
		
			else:
				self.stdscr.addstr(9, curses.COLS // 2 - (len(self.targetWord) // 2) + i, '_', curses.color_pair(3))
				finish = False

		return finish

	def checkInput(self):
		key = None
		while key not in self.alphabet:
			key = self.stdscr.getkey().upper()

		if key not in self.targetWord:
			if self.guessedLetters[key] != curses.color_pair(2):
				self.guessedLetters[key] = curses.color_pair(2)
				return self.guesses + 1

			else:
				return self.guesses

		else:
			self.guessedLetters[key] = curses.color_pair(1)
			return self.guesses
"""
	def main(self): #hier geht es weiter !!!!!!!!d
		curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

		self.guesses = 0
		Victory = False

		stdscr.clear()
		diplayAlphabet()
		targetWord(stdscr, None)
		stdscr.refresh()
		
		while self.guesses < 9 :
			galgen(stdscr, self.guesses)
			self.guesses = checkInput(stdscr, self.guesses)
			diplayAlphabet()
			Victory = targetWord(stdscr, None)
			stdscr.refresh()
			if Victory:
				break
		
		if Victory:
			galgen(stdscr, self.guesses)
			diplayAlphabet()
			targetWord(stdscr, "Win")
			stdscr.addstr(18, curses.COLS // 2 - len("You got away!") // 2, "You got away!", curses.color_pair(1))
			stdscr.refresh()

		else:
			galgen(stdscr, self.guesses)
			diplayAlphabet()
			targetWord(stdscr, "Lose")
			stdscr.addstr(18, curses.COLS // 2 - len("You are dead, boi!") // 2, "You are dead, boi!", curses.color_pair(2))
			stdscr.refresh()
		stdscr.getkey()

	if __name__=="__main__":
		wrapper(main)
"""