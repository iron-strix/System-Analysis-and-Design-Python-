import time
import scrape
import checking
import display
import guessed_list
import score
import os
import qualified

#main game logic 
def playHangman(secretWord):
    lives = 7 #the number of guesses remaining, all difficulties have 7 lives

    #print(DIFFICULTY) #debug
    #input() #debug

    #if the player has chosen easy, then difficulty == 1
    #main change from other methods is that easy web scrapes hints for the player
    if qualified.DIFFICULTY == 1:
        hint = scrape.scrape(secretWord) #web scraping to store hint

        #if there are lives remaining and the player has not won, continue game loop
        while lives > 0 and not checking.checkWinner(secretWord):
            display.display(secretWord, lives) #print game screen
            print(f"HINT: {hint}") #easy also prints the hint
            guess = input("Make a guess: ")[0].casefold() #take input
            guessed_list.addGuessedList(guess) #attempt to append input

            #first, check if the character is in the alphaList
            #if the guess is not alpha, then no other checks need
            #to be performed
            if checking.checkAlpha(guess): 
                #check if guess is in the secret and check if it hasn't already been guessed
                if not checking.checkSecretWord(secretWord, guess) and checking.checkGuessedList(guess):
                    #print("Subtracting 1 life.")
                    lives -= 1
            else:
                print("Guess is not in the alphabet. Please enter an alphabetical character (A-Z) as a guess.")
                print("No guesses will be used.")
                time.sleep(3)

        #final update after either the player has won or the player has lost
        display.display(secretWord, lives)

        #if the player has won, give them a score
        if checking.checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        guessed_list.clearGuessedList()

    #if the difficulty is not easy, then all the above logic follows except hints will not be given
    else:
        while lives > 0 and not checking.checkWinner(secretWord):
            display.display(secretWord, lives)

            guess = input("Make a guess: ")[0].casefold()
            guessed_list.addGuessedList(guess)

            #first, check if the character is in the alphaList
            #if the guess is not alpha, then no other checks need
            #to be performed
            if checking.checkAlpha(guess): 
                #check if guess is in the secret and check if it hasn't already been guessed
                if not checking.checkSecretWord(secretWord, guess) and checking.checkGuessedList(guess):
                    #print("Subtracting 1 life.")
                    lives -= 1
            else:
                print("Guess is not in the alphabet. Please enter an alphabetical character (A-Z) as a guess.")
                print("No guesses will be used.")
                time.sleep(3)

        display.display(secretWord, lives)

        if checking.checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        guessed_list.clearGuessedList()

#return true/false based on user input
#if true, player is prompted for another game
#if false the program will exit
def playAgain():
    playAgain = ''
    while playAgain != 'y' and playAgain != 'n':
        playAgain = input("Play again? Y/N").casefold()
        if playAgain != 'y' and playAgain != 'n':
            print("Please input Y/N to make a selection.")
            time.sleep(3)
    
    if playAgain == 'n':
        print("Thank you for playing!")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        return False
    else:
        return True