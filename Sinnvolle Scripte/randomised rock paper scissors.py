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
    winner = 0
    help()
    while compwin < 3 and humanwin < 3 :
        options = 'rock', 'paper', 'scissors'
        comprps = random.choice(options)
        human = input('type "rock", "paper", or "scissors"\n>')
        humanrps = human.strip().lower()
        clearConsole()
        loadingScreen()
        if humanrps == 'rock' :
            if comprps == 'rock' : 
                winner = "\u001b[33mNo one\u001b[0m"
                gameengine()
            elif comprps == 'paper' :
                compwin = compwin + 1
                winner = "\u001b[31mComputer\u001b[0m"
                gameengine()
            elif comprps == 'scissors' : 
                humanwin = humanwin + 1
                winner = "\u001b[32mPlayer\u001b[0m"
                gameengine()  
        elif humanrps == 'paper' :
            if comprps == 'rock' : 
                humanwin = humanwin + 1
                winner = "\u001b[32mPlayer\u001b[0m"
                gameengine()
            elif comprps == 'paper' : 
                winner = "\u001b[33mNo one\u001b[0m"
                gameengine()
            elif comprps == 'scissors' : 
                compwin = compwin + 1
                winner = "\u001b[31mComputer\u001b[0m"
                gameengine()
        elif humanrps == 'scissors' :
            if comprps == 'rock' : 
                compwin = compwin + 1
                winner = "\u001b[31mComputer\u001b[0m"
                gameengine()
            elif comprps == 'paper' : 
                humanwin = humanwin + 1
                winner = "\u001b[32mPlayer\u001b[0m"
                gameengine()
            elif comprps == 'scissors' : 
                winner = "\u001b[33mNo one\u001b[0m"
                gameengine()
        elif (humanrps == 'exit') :
            exit()
            quit()
        elif (humanrps == 'help') :
            help()
        elif humanrps == 'restart' :
            humanwin = 0
            compwin = 0
            NewRound()
            time.sleep(3)
            game()
            break
        elif (humanrps == 'score') or (humanrps == 'scoreboard') :
            scoreboard()
        else :
            IDontUnderstand()
    clearConsole()
    scoreboard()
    scoreboardfinal()
    while True :
        congame = input('Wanna play again? Answer "yes" or "no". \n>')
        clearConsole()
        loadingScreen()
        if congame.lower().strip() == 'yes' :
            humanwin = 0
            compwin = 0
            NewRound()
            time.sleep(3)
            game()
            break
        elif congame.lower().strip() == 'no' or 'exit' :
            clearConsole()
            exit()
            quit()
        else : #not working correctly atm, I don't know why 
            IDontUnderstand()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def loadingScreen():
    #for frame in itertools.cycle(r'-\|/-\|/'):
        #print('\r', frame, sep='', end='', flush=True)
        #time.sleep(0.2)
        #timer = timer + 1
    counttime = 0
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while (counttime != 10):
        #add animation here later
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')            # erase the last written char
        time.sleep(0.075)
        counttime = counttime + 1

#displayed texts
def exit():
    print('\n##############################################################################################')
    print('\u001b[36mHave a nice day\u001b[0m')
    print('##############################################################################################\n')
def IDontUnderstand():
    print('\n##############################################################################################')
    print("\u001b[34mI don't understand... :(\u001b[0m")
    print('##############################################################################################\n')
def NewRound():
    clearConsole()
    print('\n##############################################################################################')
    print('\u001b[35mNew Round starts in 3 Seconds!\u001b[0m')
    print('##############################################################################################\n')
def help():
    print('\n##############################################################################################')
    print("Let's play rock paper scissors!\n")
    print('The \u001b[31mComputer\u001b[0m and you, the \u001b[32mPlayer\u001b[0m will play till one of you reaches the score of 3 \u001b[33mwins\u001b[0m. \n')
    print('You can type: \n\u001b[1m"help"\u001b[0m to see this helpscreen,\n\u001b[1m"score"\u001b[0m to see the scoreboard, \n\u001b[1m"exit"\u001b[0m to exit the game, or \n\u001b[1m"restart"\u001b[0m to restart the game at \u001b[4many\u001b[0m time in the game.')
    print('##############################################################################################\n')
def gameengine() :
    clearConsole()
    print('\n##############################################################################################')
    print('The \u001b[32mPlayer\u001b[0m uses: ' + str(humanrps) + '\n' + 'The \u001b[31mcomputer\u001b[0m uses: ' + str(comprps) + '\n')
    print('Winner of this round: ' + str(winner))
    print('##############################################################################################\n')
def scoreboard() :
    print('\n-----------------------------------------------------')
    print('Scoreboard - \u001b[33mWins\u001b[0m')
    print('-----------------------------------------------------')
    print('\u001b[32mPlayer\u001b[0m: ' + str(humanwin))
    print('\u001b[31mComputer\u001b[0m: ' + str(compwin))
    print('-----------------------------------------------------\n')
def scoreboardfinal() :
    if compwin < humanwin :
        print('The \u001b[32mPlayer\u001b[0m wins the game! Congratulations!\n')
    if compwin > humanwin :
        print('The \u001b[31mComputer\u001b[0m wins the game! Hail to the king!\n')
game()