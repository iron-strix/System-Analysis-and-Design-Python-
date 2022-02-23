"""
Write a Python program to convert temperature in Celsius to Fahrenheit, and from Fahrenheit to Celsius.

What you need to do:

Ask a user to input a temperature in Celsius
Convert temperature in Celsius to Fahrenheit using the formula
F space equals space open parentheses bevelled 9 over 5 close parentheses asterisk times C space plus space 32﻿﻿
Print the temperature in Fahrenheit

Similarly, ask a user to input a temperature in Fahrenheit
Convert temperature in Fahrenheit to Celsius using the formula
C space equals space open parentheses F space minus space 32 close parentheses asterisk times space open parentheses bevelled 5 over 9 close parentheses﻿﻿
Print the temperature in Celsius

Note: You need to print your name and email address at the start of the program using print statements. You should use formatted output for printing in this Assessment.
"""
#Nigel Little
#CITP 3305 v01
#02/19/2022

print("Nigel Little - nlittle@stu.southtexascollege.edu")

c = int(input("Please input the temperature in Celcius: "))
f = ((9/5)* c + 32)
print(f"Temperature in Farenheit: {f}")

f = int(input("Please input the temperature in Farenheit: "))
c = (f - 32)*(5/9)
print(f"Temperature in Celcius: {c}")
