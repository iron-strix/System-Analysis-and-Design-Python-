#Nigel Little
#CITP 3305 v01
#03/10/2022
#Assignment 6

#open the files
file = "cats.txt"
catFile = open(file)

file = "dogs.txt"
dogFile = open(file)

#store data in variables
catData = catFile.read()
dogData = dogFile.read()

#print
print (catData)
print(dogData)

#open outfile
animalsFile = open("animals.txt", "w")

#write data
animalsFile.write(catData)
animalsFile.write("\n")
animalsFile.write(dogData)

#close
animalsFile.close()
catFile.close()
dogFile.close()