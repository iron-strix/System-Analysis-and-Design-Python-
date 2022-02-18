#Nigel Little
#CITP 3305 v01
#02/09/2022

# You need to create 4 variables: 
# keyword1, definition1, keyword2, and definition2. 
# Then assign values to these variables. 
# Basically define any two key terms, the terms will be stored in keyword1 and keyword2, and 
# their definitions will be stored in definition1, and definition2, respectively.

# Now, ask user to input 2 more keywords and their definitions in variables: 
# keyword3, keyword4, definition3, and definition4.

# You also need to create 3 more variables: 
# name, course, and module as given in the video. 
# Assign values to these variables. You do not have to ask user to input them.

# In the second part of the assignment, you need to create the following output 3 times,
# using all the three ways of printing as explained in the lecture video. 
# That is, the first output should be produced using:
# 1)string concatenation,
# 2)then using format function, 
# 3)and finally as a formatted string output. 
# The <> should be replaced by the values stored in the variables.

name = "Nigel Little"
course = "CITP 3305 v01"
module = "Module 4"

keyword1 = "hexadecimal"
definition1 = "A base 6 numbering system."
keyword2 = "octal"
definition2 = "A base 8 numbering system."

keyword3 = input("Please input a keyword: ")
definition3 = input("Please input a definition for the previous keyword: ")
keyword4 = input("Please input a 2nd keyword: ")
definition4 = input("Please input a definition for the 2nd keyword: ")

#OUTPUT:

#Using String Concatenation:
#Submission by <name>: <course> - <module>
#DICTIONARY
#    <keyword1> : <definition1>
#    <keyword2> : <definition2>
#    <keyword3> : <definition3>
#   <keyword4> : <definition4>
print("\n===========================================================")
print("Using String Concatenation:")
print("Submission by " + name + ": " + course + " - " + module)
print("DICTIONARY")
print("\t" + keyword1 + " : " + definition1)
print("\t" + keyword2 + " : " + definition2)
print("\t" + keyword3 + " : " + definition3)
print("\t" + keyword4 + " : " + definition4)

#Using format function:
#Submission by <name>: <course> - <module>
#DICTIONARY
#    <keyword1> : <definition1>
#   <keyword2> : <definition2>
#    <keyword3> : <definition3>
#    <keyword4> : <definition4>
print("\n===========================================================")
print("Using Format Function:")
print("Submission by {} : {} - {}".format(name, course, module))
print("DICTIONARY")
print("\t{} : {}".format(keyword1, definition1))
print("\t{} : {}".format(keyword2, definition2))
print("\t{} : {}".format(keyword3, definition3))
print("\t{} : {}".format(keyword4, definition4))

#As a formatted output:
#Submission by <name>: <course> - <module>
#DICTIONARY
#    <keyword1> : <definition1>
#    <keyword2> : <definition2>
#    <keyword3> : <definition3>
#    <keyword4> : <definition4>
print("\n===========================================================")
print("As a Formatted Output:")
print(f"Submission by {name} : {course} - {module}")
print(f"DICTIONARY")
print(f"\t{keyword1} : {definition1}")
print(f"\t{keyword2} : {definition2}")
print(f"\t{keyword3} : {definition3}")
print(f"\t{keyword4} : {definition4}")