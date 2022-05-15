#imports
import time
from urllib.request import urlopen
import re
import init
import hangman_game

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
        secretword = init.chooseWord(init.chooseDifficulty(), init.loadWordFile())
        hangman_game.playHangman(secretword)