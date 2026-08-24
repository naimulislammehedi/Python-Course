# Input & Output (I/O) means how a Python program receives information and shows information.

# output
print("Mehedi")

# printing text + variables 
name = "Mehedi"
age = 25

print("Name: ", name)
print("Age: ", age)

# f-strings - formatted output 
name = "John"
age = 25 
print(f"My name is {name} and I am {age} years old.")

# input() - input() alllows the user to enter information 
name = input("Enter your name: ")
print(name)

age = input("Enter your age: ")
print(type(age))

# Input + Type Conversion 
age = int(input("Enter you age: "))
print(type(age))

# Float Input 
height = float(input("Enter your height: "))
print(height)
