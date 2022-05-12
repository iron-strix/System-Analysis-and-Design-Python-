#Nigel Little
#CITP 3305 v01
#05/02/2022
#Assignment 9

def Calculator():
    select = input("Please enter an operation (addition, subtraction, multiplication, division): ")
    num1 = int(input("Please enter the first integer for operation: "))
    num2 = int(input("Please enter the second integer for operation: "))

    if select == "addition":
        print(Add(num1, num2))

    if select == "subtraction":
        print(Subtract(num1, num2))

    if select == "multiplication":
        print(Multiply(num1, num2))
    
    if select == "division":
        print(Divide(num1, num2))

def Add(num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1*num2

def Divide(num1, num2):
    return num1/num2

def vowel_count(inputString):
    inputString = inputString.lower()
    count = 0

    for char in inputString:
        if char in "aeiou":
            count = count + 1

    return count

Calculator()

print(vowel_count("I really like making programs in Python."))