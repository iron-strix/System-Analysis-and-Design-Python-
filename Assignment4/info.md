In this assignment, create a python file assign_4.py

Your script should take your name as an argument, separated by underscore. If you have a middle name, your argument should be firstname_middlename_lastname

Note, the inputs to a Python code are strings.

When executing your script, use the following command:

For Windows users: python assign_4.py firstName_middlename_lastname

For MAC users: python3 assign_4.py firstName_middlename_lastname

For example: python assign_4.py divya_bajaj

In your Python file, use functions provided in the tutorial to split the argument into two variable: gname and lname. You should split the name argument at the last occurrence of the underscore. Therefore, for argument firstname_middlename_lastname, your variables should contain values

gname = firstname_middlename

lname = lastname

Tip: you can use the function rindex() to find the last occurrence of underscore.

Finally print your output as follows:

For input firstname_middlename_lastname

The output should look like: Firstname Middlename Lastname

That is, remove the underscore between the three words, and capitalize each word. You should use strings functions to perform each of the operations.

Submit a python file for this assignment.