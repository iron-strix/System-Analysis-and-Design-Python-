#Nigel Little
#CITP 3305 v01
#04/3/2022
#Assignment 7 Extra Credit

#get input
userString = input("Please input a string. This program will check if it's a palindrome: ")
reverseString = ""

#loop to extact characters in reverse and store
for char in userString:
    reverseString = char + reverseString

#all to lowercase
reverseString = reverseString.casefold()
userString = userString.casefold()

#remove all spaces
reverseString = reverseString.replace(" ", "")
userString = userString.replace(" ", "")

#check if palindrome
if reverseString == userString:
    print(True)

else:
    print(False)
