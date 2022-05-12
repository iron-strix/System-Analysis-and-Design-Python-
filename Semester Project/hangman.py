#Nigel Little
#CITP 3305v01
#03/05/2022
#hangman test

import random
import os
import time
from urllib.request import urlopen
import re

#define where the words file is
WORDLIST_FILE = "engmix_removed.txt"

#create a global guessedList variable for functions to use
guessedList = []

#create a global difficulty
DIFFICULTY = 0

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

    #print("  ", len(wordlist), "words loaded.")
    return wordlist

#have user choose difficulty, returns int
def chooseDifficulty():
    print(f"Please choose the level of difficulty desired.")
    print(f"1. Easy - Words are 6 characters or less. Hints are given.")
    print(f"2. Medium - Words are 9 characters or less. No hints are given.")
    print(f"3. Hard - Words are 12 characters or less. No hints are given.")
    difficulty = input()
    global DIFFICULTY 
    DIFFICULTY = int(difficulty)
    return int(difficulty)

#choose a word at random based on difficulty from wordlist
def chooseWord(difficulty, wordlist):
    #print(f"difficulty chosen was {difficulty}")

    #DEBUG
    cheatMode = False

    if cheatMode:
        return input("CHEAT MODE ENABLED\nPlease input your own word: ")

    if int(difficulty) == 1:
        easylist = []
        for item in wordlist:
            if len(item[0]) <= 6 and len(item[0]) > 2:
                easylist.append(item[0])
        #easylist = [x for x in wordlist if (len(str(x)) < 7)]
        #easylist[:] = [x for x in easylist if (len(str(x)) < 2)]
        #easylist = list(filter(lambda x : ((len(str(x)) < 7) and (len(str(x)) > 2)), wordlist))
        #print("  ", len(easylist), "words loaded.")
        return random.choice(easylist)

    elif int(difficulty) == 2:
        mediumlist = []
        for item in wordlist:
            if len(item[0]) <= 9 and len(item[0]) > 2:
                mediumlist.append(item[0])
        #print("  ", len(mediumlist), "words loaded.")
        return random.choice(mediumlist)

    else:
        hardlist = []
        for item in wordlist:
            if len(item[0]) <= 12 and len(item[0]) > 5:
                hardlist.append(item[0])
        #print("  ", len(hardlist), "words loaded.")
        return random.choice(hardlist)

#web scraping
#search
def scrape(secretWord):  
    try:
        url = 'https://www.dictionary.com/browse/'
        term = secretWord.casefold()
        url += term
        #print(f"Searching {url} ...") #debug

        #attempt to open url, will time out after 5 seconds
        page = urlopen(url, None, 5)

        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        #match_results = re.search(pattern, html, re.IGNORECASE)
        #result = match_results.group()
        #result = re.sub("<.*?>", "", result) #remove HTML tags
        #result = result.replace("<span class=\"luna-example", "", 1)
        #return str(result)
    
        #pattern 3
        try:
            pattern = "value=\"1\".*?</div>"
            match_results = re.search(pattern, html, re.IGNORECASE)
            #print(match_results)
            result = match_results.group()
            #print(result) #debug
            pattern2 = "<span class=\"luna-example"
            
            #check to remove useage of word, can spoil the secretWord
            if pattern2 in result:
                result = re.sub("<span class=\"luna-example.*?</span>", "", result)
            
            result = re.sub("<.*?>", "", result) #remove HTML tags
            
            result = re.sub("value=\"1\"","", result) #remove value=1
            result = re.sub("class=.*?>", "", result)
            result = result.replace(":", "", -1)
            return str(result)
        except AttributeError as e:
            print("Pattern 3 failed.")
            print(e)
            #print(match_results)

        #pattern 1
        try:
            pattern = "<div class=\"default-content\">.*?<span class=\"luna-example"
            match_results = re.search(pattern, html, re.IGNORECASE)
            result = match_results.group()
            result = re.sub("<.*?>", "", result) #remove HTML tags
            result = result.replace("<span class=\"luna-example", "", 1)
            return str(result)
        except AttributeError as e:
            print("Pattern 1 failed.")
            print(e)
            #print(match_results)

        #pattern 2
        try:
            pattern = "<section id=\"top-definitions-section\".*?value=\"2\""
            match_results = re.search(pattern, html, re.IGNORECASE)
            result = match_results.group()
            result = re.sub("<.*?>", "", result) #remove HTML tags
            result = result.replace(":", "", -1)
            return str(result)
        except AttributeError as e:
            print("Pattern 2 failed.")
            print(e)
            #print(match_results)

    # ISSUES WITH ERRORS BEING THROWN
    # HTML LAYOUT IS DIFFERENT FROM PAGE TO PAGE
    # MAY NEED MULTIPLE REGEX TRY/CATCH BLOCKS
    except Exception as e:
        print("Hint URL failed!")
        print (e)

        print("\n\nRestarting the game with a new word...")
        #wait a few seconds to restart

        time.sleep(5)
        secretword = chooseWord(chooseDifficulty(), loadWordFile())
        playHangman(secretword)

#check if guessed character is in word
def checkSecretWord(secretWord, guess):
    if secretWord != None and guess in secretWord:
        print(f"{guess} found in the word!")
        time.sleep(1)
        return True
    else:
        print(f"{guess} is NOT in the word.")
        time.sleep(1)
        return False

#check if character guessed is in list
def checkGuessedList(guess):
    global guessedList
    for item in guessedList:
        if item == guess:
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

    os.system('cls' if os.name == 'nt' else 'clear')

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
def score(secretWord, lives):
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

    return score*lives

#main game logic 
def playHangman(secretWord):
    global DIFFICULTY
    lives = 7

    #print(DIFFICULTY) #debug
    #input() #debug

    if DIFFICULTY == 1:
        hint = scrape(secretWord)
        while lives > 0 and not checkWinner(secretWord):
            display(secretWord, lives)
            print(f"HINT: {hint}")
            guess = input("Make a guess: ")[0]
            addGuessedList(guess)

            if not checkSecretWord(secretWord, guess) and checkGuessedList(guess):
                #print("Subtracting 1 life.")
                lives -= 1

        display(secretWord, lives)

        if checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        clearGuessedList()

    else:
        while lives > 0 and not checkWinner(secretWord):
            display(secretWord, lives)

            guess = input("Make a guess: ")[0]
            addGuessedList(guess)

            if not checkSecretWord(secretWord, guess) and checkGuessedList(guess):
                #print("Subtracting 1 life.")
                lives -= 1

        display(secretWord, lives)

        if checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        clearGuessedList()

def main():
    playing = True
    while playing:
        secretWord = chooseWord(chooseDifficulty(), loadWordFile())
        #secretWord = input("DEBUG: Input secret word. Please disable this feature to actually play a game.")
        #print(f"I'm cheating. secretWord is {secretWord}")
        playHangman(secretWord)
        
        playAgain = ''
        while playAgain != 'y' and playAgain != 'n':
            playAgain = input("Play again? Y/N").casefold()
        
        if playAgain == 'n':
            playing = False
    
main()