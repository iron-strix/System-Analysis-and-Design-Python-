import os
import init
import hangman_game

playing = True
while playing:
    secretWord = init.chooseWord(init.chooseDifficulty(), init.loadWordFile()) #get a random word out of the lists and prompt the player to choose a difficulty
    #secretWord = input("DEBUG: Input secret word. Please disable this feature to actually play a game.")
    #print(f"I'm cheating. secretWord is {secretWord}")
    #time.sleep(3)
    hangman_game.playHangman(secretWord) #using the random secretword, play a game of hangman with the chosen difficulty. Difficulty is global and is not passed
    
    playing = hangman_game.playAgain() #prompt to play again
    os.system('cls' if os.name == 'nt' else 'clear') #finally, clean up screen