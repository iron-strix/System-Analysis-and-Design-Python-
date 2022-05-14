#Nigel Little
#CITP 3305v01
#03/05/2022
#hangman

#this program will let the user play a game of hangman
#features include: difficulty selection, web scraped hints from dictionary.com
#replay selection, 85k words, and user scoring

#imports
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

#load the words from file, return list of words
#list of words currently used is aprox 85k words
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

#have user choose difficulty, returns int based on selection
def chooseDifficulty():
    print(f"Please choose the level of difficulty desired.")
    print(f"1. Easy - Words are 6 characters or less. Hints are given.")
    print(f"2. Medium - Words are 9 characters or less. No hints are given.")
    print(f"3. Hard - Words are 12 characters or less. No hints are given.")
    difficulty = input()
    global DIFFICULTY 
    DIFFICULTY = int(difficulty)
    return int(difficulty)

#choose a word at random based on difficulty from wordlist, returns a single string (secretword)
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
#searches dictionary.com for the secretword and trims the url (if found) using regex
#returns a string that *should* be just the definition of the word
#due to different page layouts and imperfect regex (regex is hard, okay?), results may vary
#so far pattern3 has proven the most reliable so it is the first regex attempted
#if the regex pattern fails it returns a NoneType exception, hence the numerous try/except blocks
#if the url 404, it likewise raises an exception
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

        # ISSUES WITH ERRORS BEING THROWN
        # HTML LAYOUT IS DIFFERENT FROM PAGE TO PAGE
        # MAY NEED MULTIPLE REGEX TRY/CATCH BLOCKS
        
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

    except Exception as e:
        print("Hint URL failed!")
        print (e)

        print("\n\nRestarting the game with a new word...")
        #wait a few seconds to restart

        time.sleep(5)
        secretword = chooseWord(chooseDifficulty(), loadWordFile())
        playHangman(secretword)

#check if guessed character is in word
#if character is found returns true/false
def checkSecretWord(secretWord, guess):
    if secretWord != None and guess in secretWord:
        print(f"{guess} found in the word!")
        time.sleep(1)
        return True
    else:
        print(f"{guess} is NOT in the word.")
        time.sleep(2)
        return False

#checks if guess is in the alphabet, non-alpha characters aren't valid inputs
#returns true if the guess is an alpha character, false if it is not
def checkAlpha(guess):
    alphaList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for item in alphaList:
        if item == guess.casefold():
            return True

    return False

#check if guess has already been guessed
#returns true if the guess is already in guessedList, false if not
def checkGuessedList(guess):
    global guessedList
    
    for item in guessedList:
        if item == guess:
            #print(f"{guess} has already been guessed!")
            return True
    return False
    
#keep track of which letters have been guessed
#calls checkGuessedList and checkAlpha to first check if it should be added to guessedList
#since guessedList is used to create display, this is user facing and needs the extra check for things
#to make sense for the user
def addGuessedList(guess):
    global guessedList
    if not checkGuessedList(guess) and checkAlpha(guess):
        guessedList.append(guess)

#check guessedList vs secretWord
#if all characters in the secretWord are also contained within guessedList then
#the comprehension will return true/true/true/true etc for each character
#essentially creating a new list of true/false values
#if any of the characters fails to be found, the one false entry will cause the all() statement to return false
def checkWinner(secretWord):
    global guessedList
    matchedList = [characters in guessedList for characters in secretWord]
    #print(matchedList)
    #print(all(matchedList))
    return all(matchedList)

#clear guesses when game is done
#this list is user facing and used for display
def clearGuessedList():
    global guessedList
    guessedList.clear()

#display for user
#main output to screen to play game of hangman
def display(secretWord, lives):
    global guessedList

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
        if char in guessedList:
            print(f"{char} ", end ='')
        else:
            print("_ ", end ='')
    
    #numerical number of lives remaining
    print(f"\t{lives} guesses remaining.")

    #display characters already guessed
    print("\nGuessed characters: ", end='')
    for item in guessedList:
        print(f"{item[0]} ", end='')
    print("\n")

#calculate score
#score dictionary is based on how common each of the characters is in typed words
#based on a study of books that were transcribed from books to digital format
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
    
    #sum the characters to provide scoring
    for item in scoreDict:
        if item in secretWord:
            score += scoreDict[item]

    return score*lives

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

#main game logic 
def playHangman(secretWord):
    global DIFFICULTY
    lives = 7 #the number of guesses remaining, all difficulties have 7 lives

    #print(DIFFICULTY) #debug
    #input() #debug

    #if the player has chosen easy, then difficulty == 1
    #main change from other methods is that easy web scrapes hints for the player
    if DIFFICULTY == 1:
        hint = scrape(secretWord) #web scraping to store hint

        #if there are lives remaining and the player has not won, continue game loop
        while lives > 0 and not checkWinner(secretWord):
            display(secretWord, lives) #print game screen
            print(f"HINT: {hint}") #easy also prints the hint
            guess = input("Make a guess: ")[0].casefold() #take input
            addGuessedList(guess) #attempt to append input

            #first, check if the character is in the alphaList
            #if the guess is not alpha, then no other checks need
            #to be performed
            if checkAlpha(guess): 
                #check if guess is in the secret and check if it hasn't already been guessed
                if not checkSecretWord(secretWord, guess) and checkGuessedList(guess):
                    #print("Subtracting 1 life.")
                    lives -= 1
            else:
                print("Guess is not in the alphabet. Please enter an alphabetical character (A-Z) as a guess.")
                print("No guesses will be used.")
                time.sleep(3)

        #final update after either the player has won or the player has lost
        display(secretWord, lives)

        #if the player has won, give them a score
        if checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        clearGuessedList()

    #if the difficulty is not easy, then all the above logic follows except hints will not be given
    else:
        while lives > 0 and not checkWinner(secretWord):
            display(secretWord, lives)

            guess = input("Make a guess: ")[0].casefold()
            addGuessedList(guess)

            #first, check if the character is in the alphaList
            #if the guess is not alpha, then no other checks need
            #to be performed
            if checkAlpha(guess): 
                #check if guess is in the secret and check if it hasn't already been guessed
                if not checkSecretWord(secretWord, guess) and checkGuessedList(guess):
                    #print("Subtracting 1 life.")
                    lives -= 1
            else:
                print("Guess is not in the alphabet. Please enter an alphabetical character (A-Z) as a guess.")
                print("No guesses will be used.")
                time.sleep(3)

        display(secretWord, lives)

        if checkWinner(secretWord):
            print(f"\nCongrats, you win! Here's your score: {score(secretWord, lives)}")
        else:
            print(f"\nSorry, the word was {secretWord.upper()}. Better luck next time!")
        
        clearGuessedList()

#main calls the main game logic and also handles the game state (playing/not playing)
def main():
    playing = True
    while playing:
        secretWord = chooseWord(chooseDifficulty(), loadWordFile()) #get a random word out of the lists and prompt the player to choose a difficulty
        #secretWord = input("DEBUG: Input secret word. Please disable this feature to actually play a game.")
        #print(f"I'm cheating. secretWord is {secretWord}")
        #time.sleep(3)
        playHangman(secretWord) #using the random secretword, play a game of hangman with the chosen difficulty. Difficulty is global and is not passed
        
        playing = playAgain() #prompt to play again
        os.system('cls' if os.name == 'nt' else 'clear') #finally, clean up screen
  
main()