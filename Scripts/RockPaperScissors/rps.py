import random
import os
import time
import itertools
import sys
def game():
    global humanwin
    global compwin
    global winner
    global humanrps
    global comprps
    humanwin = 0
    compwin = 0
    winner = None
    clearConsole()
    help()
    while compwin < 3 and humanwin < 3:
        options = 'rock', 'paper', 'scissors'
        comprps = random.choice(options)
        humanrps = input('type "\u001b[35mrock\u001b[0m", "\u001b[33mpaper\u001b[0m", or "\u001b[36mscissors\u001b[0m"\n>').strip().lower()
        clearConsole()
        loadingScreen()
        if (humanrps == 'rock' and comprps == 'scissors') or (humanrps == 'paper' and comprps == 'rock') or (humanrps == 'scissors' and comprps == 'paper'):
                humanwin = humanwin + 1
                winner = "\u001b[32mPlayer\u001b[0m"
                colourAnswers()
                gameengine()
        elif humanrps == comprps:
            winner = "\u001b[33mNo one\u001b[0m"
            colourAnswers()
            gameengine()
        elif humanrps == 'exit':
            exit()
            quit()
        elif humanrps == 'help':
            help()
        elif humanrps == 'restart':
            humanwin = 0
            compwin = 0
            NewRound()
            time.sleep(0.5)
            game()
            break
        elif (humanrps == 'score') or (humanrps == 'scoreboard'):
            scoreboard()
        elif humanrps not in options:
            IDontUnderstand()
        else:
            compwin = compwin + 1
            winner = "\u001b[31mComputer\u001b[0m"
            colourAnswers()
            gameengine()
    clearConsole()
    scoreboard()
    finalresult()
    while True:
        print('\n##############################################################################################')
        congame = input('Wanna play again? Answer "\u001b[35myes\u001b[0m" or "\u001b[36mno\u001b[0m".\n>')
        clearConsole()
        loadingScreen()
        if congame.lower().strip() == 'yes':
            humanwin = 0
            compwin = 0
            NewRound()
            time.sleep(0.5)
            game()
            break
        elif congame.lower().strip() == 'no' or congame.lower().strip() == 'exit': 
            clearConsole()
            exit()
            quit()
        else : 
            IDontUnderstand()

#game engine
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def loadingScreen():
    counttime = 0
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while (counttime != 10):
        #add animation here later
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')            # erase the last written char
        time.sleep(0.075)
        counttime = counttime + 1
def colourAnswers():
    global humanrps
    global comprps
    if humanrps == "rock" :
        humanrps = '\u001b[35mrock\u001b[0m'
    elif humanrps == "paper" :
        humanrps = '\u001b[33mpaper\u001b[0m'
    else :
        humanrps = '\u001b[36mscissors\u001b[0m'
    if comprps == "rock" :
        comprps = '\u001b[35mrock\u001b[0m'
    elif comprps == "paper" :
        comprps = '\u001b[33mpaper\u001b[0m'
    else :
        comprps = '\u001b[36mscissors\u001b[0m'

#printing
def exit():
    clearConsole()
    print('\n##############################################################################################')
    print('\u001b[36mHave a nice day :)\u001b[0m')
    print('##############################################################################################\n')
def IDontUnderstand():
    clearConsole()
    print('\n##############################################################################################')
    print("\u001b[33mI don't understand you... :(\u001b[0m")
    print('##############################################################################################\n')
def NewRound(): #this should be improved in the future
    clearConsole()
    for i in range(3, 0, -1):
        print('\u001b[35mNew Round starts in \u001b[0m' + str(i), end = '\r')
        time.sleep(1)
def help():
    clearConsole()
    print('\n##############################################################################################')
    print("Let's play rock paper scissors!\n")
    print('The \u001b[31mComputer\u001b[0m and you, the \u001b[32mPlayer\u001b[0m, will play till one of you reaches the score of 3 \u001b[34mWins\u001b[0m. \n')
    print('You can type: \n\u001b[1m"help"\u001b[0m to see this helpscreen,\n\u001b[1m"score"\u001b[0m to see the scoreboard, \n\u001b[1m"restart"\u001b[0m to restart the game, or \n\u001b[1m"exit"\u001b[0m to exit the game at \u001b[4many\u001b[0m time in the game.')
    print('##############################################################################################\n')
def gameengine():
    clearConsole()
    print('\n##############################################################################################')
    print('The \u001b[32mPlayer\u001b[0m uses: '  + str(humanrps) + '\n' + 'The \u001b[31mcomputer\u001b[0m uses: ' + str(comprps) + '\n')
    print('\n\u001b[1mWinner\u001b[0m of this round: ' + str(winner))
    print('##############################################################################################\n')
def scoreboard():
    clearConsole()
    print('\n-----------------------------------------------------')
    print('Scoreboard - \u001b[34mWins\u001b[0m')
    print('-----------------------------------------------------')
    print('\u001b[32mPlayer\u001b[0m: ' + str(humanwin))
    print('\u001b[31mComputer\u001b[0m: ' + str(compwin))
    print('-----------------------------------------------------\n')
def finalresult():
    if compwin < humanwin:
        print('The \u001b[32mPlayer\u001b[0m wins the game! Congratulations!\n')
    if compwin > humanwin:
        print('The \u001b[31mComputer\u001b[0m wins the game! Hail to the king!\n')
game()