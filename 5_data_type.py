# Python Data Types 
# A data type tells Python what kind of value a variable contains 
name = "Mehedi"
age = 25
height = 5.8
is_student = True

# numeric data types 
age = 25
temperature = -5
students = 100

# float - floating point number 
price = 99.50 
height = 5.8
temperature = 36.5

# complex - complex number 
z = 3 + 4j
print(z)

# Boolean data type - bool 
is_student = True
is_married = False 

# str - string data type 
name = "Mehedi"
country = "Bangladesh"
message = "Hello Python"

# list - a list stores multiple values in a single variable  
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
fruits[1] = "Orange"
print(fruits)

# Tuple - a tuple is similar to a list, but it is immutable 
coordinates = (10, 20)
print(coordinates[0])
# you cannot normally change an item 
# coordinates[0] = 50 # error 

# set - a set stores unique values 
numbers = {1, 2, 3, 4}
print(numbers)

# dictionary - a dictionary stores data as key-value pairs 
student = {
    "name": "Mehedi", 
    "age": 25, 
    "country": "Bangladesh"
}
# access a value using its key 
print(student["name"])

# None - none means no value or absense of a value 
result = None
price(type(result))