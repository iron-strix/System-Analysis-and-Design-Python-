#imports
import qualified
import time

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
    
    for item in qualified.guessedList:
        if item == guess:
            #print(f"{guess} has already been guessed!")
            return True
    return False

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

#check guessedList vs secretWord
#if all characters in the secretWord are also contained within guessedList then
#the comprehension will return true/true/true/true etc for each character
#essentially creating a new list of true/false values
#if any of the characters fails to be found, the one false entry will cause the all() statement to return false
def checkWinner(secretWord):
    qualified.guessedList
    matchedList = [characters in qualified.guessedList for characters in secretWord]
    #print(matchedList)
    #print(all(matchedList))
    return all(matchedList)