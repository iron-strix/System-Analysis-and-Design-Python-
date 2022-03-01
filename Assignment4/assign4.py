#Nigel Little
#CITP 3305 v01
#02/23/2022
#Assignment 4

#module to allow argument variables
from sys import argv

#store argument variable as a string
#using argv at index 1 because using just argv gave a list with both
# assign4.py and Nigel_Alexander_Little as values
fullName = argv[1]
#print(f"{fullName}")

#split argument into list from the first underscore from the right
fullName = fullName.rsplit("_", 1)

#assign values in list into string variables
#casefold to make it so that upper or lowercase doesn't matter, we'll format later
gname = fullName[0].casefold()
lname = fullName[1].casefold()

#replace that pesky underscore in gname
gname = gname.replace('_', ' ')

#capitalize
#since gname is two words and we want both capital, title() is used
gname = gname.title()
lname = lname.capitalize()

#print
print(f"{gname} {lname}")