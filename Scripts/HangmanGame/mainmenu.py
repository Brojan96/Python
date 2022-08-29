#from hangman_game.py import main
#from Python.Scripts.PythonToolbox.PythonToolbox import clearConsole
import os
import time
from hangman_game import Hangman
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

choice = None
easy = ['easy', '1']
normal = ['normal', '2', '']
hard = ['hard', '3']
slashes = ""

if os.name in ('nt', 'dos'):
    slashes = "\\"

else:
    slashes = "/"

while True:
    clearConsole()  
    choice = input("What gamemode do you want to play?\nEasy [1]\nNormal [2]\nHard [3]\n\nType the \033[4mname\u001b[0m or the \033[4mnumber\u001b[0m of the difficulty you want to select.\nType 'exit' to exit the game.\n>").strip().lower()

    if choice in easy:
        print('\nYou choose easy difficulty.\nLoading the game now.')
        f = open (os.path.dirname(__file__) + "{}wordlists{}wordlist_easy.txt".format(slashes, slashes), "r")
        targetWord = random.choice(f.read().splitlines()).upper()
        hangman = Hangman(targetWord)
        hangman.runGame()
    elif choice in normal:
        print('\nYou choose normal difficulty.\nLoading the game now.')
        f = open (os.path.dirname(__file__) + "{}wordlists{}wordlist_normal.txt".format(slashes, slashes), "r")
        targetWord = random.choice(f.read().splitlines()).upper()
        hangman = Hangman(targetWord)
        hangman.runGame()
    elif choice in hard:
        print('\nYou choose hard difficulty.\nLoading the game now.')
        f = open (os.path.dirname(__file__) + "{}wordlists{}wordlist_hard.txt".format(slashes, slashes), "r")
        targetWord = random.choice(f.read().splitlines()).upper()
        hangman = Hangman(targetWord)
        hangman.runGame()
    elif choice == "exit":
        break
    else:
        print("\nPlease enter a \033[4mvalid\u001b[0m input.")
        time.sleep(3)