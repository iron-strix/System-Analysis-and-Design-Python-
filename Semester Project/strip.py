WORDLIST_FILE = "engmix.txt"

inFile = open(WORDLIST_FILE, 'r')

wordlist = []

while True:
    line = inFile.readline()
    if not line:
        break
    wordlist.append(line.split())

WORDLIST_FILE = "editedlist.txt"
inFile = open(WORDLIST_FILE, 'r')

removelist = []

while True:
    line = inFile.readline()
    if not line:
        break
    removelist.append(line.split())

textfile = open("engmix_removed.txt", "w")
for item in removelist:
    if item in wordlist:
        wordlist.remove(item)

for item in wordlist:
    textfile.write(item[0] + "\n")
textfile.close()