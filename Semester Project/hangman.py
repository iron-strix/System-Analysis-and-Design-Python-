#Nigel Little
#CITP 3305v01
#03/05/2022
#hangman test

import random

#define where the words file is
WORDLIST_FILE = "words.txt"

#create a global guessedList variable for functions to use
guessedList = []

#load the words from file
def loadWordFile():
    inFile = open(WORDLIST_FILE, 'r')
    wordlist = []
    
    while True:
        line = inFile.readline()
        if not line:
            break
        wordlist.append(line.split())

    wordlist.sort(key=len)

    print("  ", len(wordlist), "words loaded.")
    
    return wordlist

#have user choose difficulty, returns int
def chooseDifficulty():
    print(f"Please choose the level of difficulty desired.")
    print(f"1. Easy - Words are 6 characters or less. Hints are given.")
    print(f"2. Medium - Words are 9 characters or less. No hints are given.")
    print(f"3. Hard - Words are 12 characters or less. No hints are given.")
    difficulty = input()
    return int(difficulty)

#choose a word at random based on difficulty from wordlist
def chooseWord(difficulty, wordlist):
    
    print(f"difficulty chosen was {difficulty}")

    if int(difficulty) == 1:
        easylist = []
        for item in wordlist:
            if len(item[0]) <= 6 and len(item[0]) > 2:
                easylist.append(item[0])
        #easylist = [x for x in wordlist if (len(str(x)) < 7)]
        #easylist[:] = [x for x in easylist if (len(str(x)) < 2)]

        #easylist = list(filter(lambda x : ((len(str(x)) < 7) and (len(str(x)) > 2)), wordlist))
        print("  ", len(easylist), "words loaded.")
        return random.choice(easylist)

    elif int(difficulty) == 2:
        mediumlist = []
        for item in wordlist:
            if len(item[0]) <= 9 and len(item[0]) > 2:
                mediumlist.append(item[0])
        print("  ", len(mediumlist), "words loaded.")
        return random.choice(mediumlist)

    else:
        hardlist = []
        for item in wordlist:
            if len(item[0]) <= 12 and len(item[0]) > 5:
                hardlist.append(item[0])
        print("  ", len(hardlist), "words loaded.")
        return random.choice(hardlist)

#check if guessed character is in word
def checkSecretWord(secretWord, guess):
    if secretWord != None and guess in secretWord:
        #print(f"{guess} found in {secretWord}")
        return True
    else:
        print(f"{guess} is NOT in the word.")
        return False

#check if character guessed is in list
def checkGuessedList(guess):
    global guessedList
    for item in guessedList:
        if item[0] == guess:
            #print(f"{guess} has already been guessed!")
            return True
    return False
    
#keep track of which letters have been guessed
#calls checkGuessedList to see first
def addGuessedList(guess):
    global guessedList
    if not checkGuessedList(guess):
        guessedList.append(guess)

#check guessedList vs secretWord
def checkWinner(secretWord):
    global guessedList
    matchedList = [characters in guessedList for characters in secretWord]
    #print(matchedList)
    #print(all(matchedList))
    return all(matchedList)

#clear guesses when game is done
def clearGuessedList():
    global guessedList
    guessedList.clear()

#display for user
def display(secretWord, lives):
    global guessedList

    for char in str(secretWord):
        if char in guessedList:
            print(f"{char} ", end ='')
        else:
            print("_ ", end ='')
    print(f"\t{lives} guesses remaining.")

    print("\nGuessed characters: ", end='')
    for item in guessedList:
        print(f"{item[0]} ", end='')
    print("\n")

#calculate score
def score(secretWord):
    score = 0
    scoreDict = {
        'e' : 10,
        't' : 20,
        'a' : 30,
        'i' : 30,
        'n' : 30,
        'o' : 30,
        's' : 30,
        'h' : 40,
        'r' : 45,
        'd' : 50,
        'l' : 55,
        'u' : 60,
        'c' : 70,
        'm' : 70,
        'f' : 80,
        'w' : 90,
        'y' : 90,
        'g' : 100,
        'p' : 100,
        'b' : 105,
        'v' : 110,
        'k' : 125,
        'q' : 135,
        'j' : 140,
        'x' : 140,
        'z' : 200
    }
    
    for item in scoreDict:
        if item in secretWord:
            score += scoreDict[item]
    return score

#main game logic 
def playHangman(secretWord):
    lives = 5

    while lives > 0 and not checkWinner(secretWord):
        display(secretWord, lives)

        guess = input("Make a guess: ")[0]
        addGuessedList(guess)

        if not checkSecretWord(secretWord, guess) and checkGuessedList(guess):
            #print("Subtracting 1 life.")
            lives -= 1

    display(secretWord, lives)

    if checkWinner(secretWord):
        print(f"\nCongrats, you win! Here's your score: {score(secretWord)}")
    else:
        print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
    
    clearGuessedList()

def main():
    playing = True
    while playing:
        secretWord = chooseWord(chooseDifficulty(), loadWordFile())
        #print(f"I'm cheating. secretWord is {secretWord}")
        playHangman(secretWord)
        
        playAgain = ''
        while playAgain != 'y' and playAgain != 'n':
            playAgain = input("Play again? Y/N").casefold()
        
        if playAgain == 'n':
            playing = False
    
main()