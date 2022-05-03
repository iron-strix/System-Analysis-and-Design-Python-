#Nigel Little
#CITP 3305 v01
#04/3/2022
#Assignment 7

#get input
userString = input("Please input a word. This program will check if it's a palindrome: ")
reverseString = ""

#loop to extact characters in reverse and store
for char in userString:
    reverseString = char + reverseString

#check if palindrome
if reverseString == userString:
    print(True)

else:
    print(False)
