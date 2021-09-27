import random
import os

def hangman_game() :
    guesses = 0
    #random.choices()
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
            print('hello')
        #check if answer is 
        #if answer == false :
          #  guesses = guesses + 1
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
hangman_game()