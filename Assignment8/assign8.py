#Nigel Little
#CITP 3305 v01
#04/18/2022
#Assignment 8

#lists
colors1 = ['red', 'blue', 'yellow', 'green', 'purple']
colors2 = ['mauve', 'cyan', 'maroon', 'sage', 'plum', 'lavender', 'gold']
colors1.extend(colors2)
#print(colors1)

#using set()
cars = ['Acura', 'Audi', 'BMW', 'Cadillac', 'Ford','GMC', 'Honda', 'Jaguar', 'Lexus', 'Maserati']
cars = set(cars)
#print(cars)

#dictionary
employee = {
    "name": "Nigel Little",
    "age": "28",
    "department": "Sales"
}
#print(employee)

#removes indexes 4,5,6,and 7 from colors1
del colors1[4:8]

#print
print(colors1)
print(cars)
print(employee)