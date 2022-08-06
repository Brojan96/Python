#from hangman_game.py import main
#from Python.Scripts.PythonToolbox.PythonToolbox import clearConsole
import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

choice = None
easy = ['easy', '1']
normal = ['normal', '2', '']
hard = ['hard', '3']
allchoices = easy + normal + hard

while choice not in allchoices:
    clearConsole()  
    choice = input("What gamemode do you want to play?\nEasy [1]\nNormal [2]\nHard [3]\n\nType the \033[4mname\u001b[0m or the \033[4mnumber\u001b[0m of the difficulty you want to select.\nType 'exit' to exit the game.\n>").strip().lower()

    if choice in easy:
        print('\nYou choose easy difficulty.\nLoading the game now.')
        time.sleep(3)
        #load the hangman game and send over the difficulty value
    elif choice in normal:
        print('\nYou choose normal difficulty.\nLoading the game now.')
        time.sleep(3)
    elif choice in hard:
        print('\nYou choose hard difficulty.\nLoading the game now.')
        time.sleep(3)
    elif choice == "exit":
        quit()
    else:
        print("\nPlease enter a \033[4mvalid\u001b[0m input.")
        time.sleep(3)