import os
import qualified

#display for user
#main output to screen to play game of hangman
def display(secretWord, lives):
    qualified.guessedList

    #first, clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #check for which ascii art to display
    #this is relative to how many lives are
    #remaining for the player
    if (lives == 7):
            print("_________")
            print("|	 |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")

    elif (lives == 6):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|")
            print("|")
            print("|")
            print("|________")
    
    elif (lives == 5):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	 |")
            print("|")
            print("|")
            print("|________")
    
    elif (lives == 4):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	 |")
            print("|	 |")
            print("|")
            print("|________")
    
    elif (lives == 3):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|")
            print("|	 |")
            print("|")
            print("|________")
    
    elif (lives == 2):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|")
            print("|________")
    
    elif (lives == 1):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/")
            print("|________")
    
    elif (lives == 0):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")

    #display which characters are correctly guessed in the word
    #otherwise, display "_", eg beach could be "b _ _ c h" if
    #"e" and "a" have not been guessed
    for char in str(secretWord):
        if char in qualified.guessedList:
            print(f"{char} ", end ='')
        else:
            print("_ ", end ='')
    
    #numerical number of lives remaining
    print(f"\t{lives} guesses remaining.")

    #display characters already guessed
    print("\nGuessed characters: ", end='')
    for item in qualified.guessedList:
        print(f"{item[0]} ", end='')
    print("\n")