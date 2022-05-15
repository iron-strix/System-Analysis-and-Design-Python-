#imports
import random
import qualified

#load the words from file, return list of words
#list of words currently used is aprox 85k words
def loadWordFile():
    inFile = open(qualified.WORDLIST_FILE, 'r')
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
    qualified.DIFFICULTY = int(difficulty)
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