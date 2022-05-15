import checking
import qualified

#keep track of which letters have been guessed
#calls checkGuessedList and checkAlpha to first check if it should be added to guessedList
#since guessedList is used to create display, this is user facing and needs the extra check for things
#to make sense for the user
def addGuessedList(guess):
    qualified.guessedList
    if not checking.checkGuessedList(guess) and checking.checkAlpha(guess):
        qualified.guessedList.append(guess)

#clear guesses when game is done
#this list is user facing and used for display
def clearGuessedList():
    qualified.guessedList
    qualified.guessedList.clear()