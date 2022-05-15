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