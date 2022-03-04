#Nigel Little
#CITP 3305 v01
#03/01/2022
#Assignment 5

print(f"================================================================================================")
print(f"\tThis program will take primary colors and mixes them to create secondary colors.")
print(f"================================================================================================\n")

#prompt user for 2 primary colors (red, yellow, blue)
color1 = input("Please input a primary color (red, yellow, blue): ")
color2 = input("Please input a second primary color (red, yellow, blue): ")

#format input to lowercase
#reduces errors from silly things like capitalization
color1 = color1.casefold()
color2 = color2.casefold()

colorList = [color1, color2]
output = 'no value'

#based on user input, calculate the mix of their primary colors
#secondary colors are: orange, purple, green

#using match logic
#match colorList:
#    case (['red', 'yellow']|['yellow', 'red']): output = 'orange'
#    case (['red', 'blue']|['blue', 'red']): output = 'purple'
#    case (['blue', 'yellow']|['yellow', 'blue']): output = 'green'

#using if elif logic
if colorList == ['red', 'yellow'] or colorList == ['yellow', 'red']:
    output = 'orange'
elif colorList == ['red', 'blue'] or colorList == ['blue', 'red']:
    output = 'purple'
elif colorList == ['blue', 'yellow'] or colorList == ['yellow', 'blue']:
    output = 'green'

#display
if output == 'orange' or output == 'green' or output == 'purple':
    print(f"\nMixing {color1} and {color2} makes {output}!")
#error checking 
else:
    print(f"Something went wrong... are you sure {color1} and {color2} are both primary colors?")
    exit()