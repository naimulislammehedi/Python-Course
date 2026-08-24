# Basic Python Program 
print("Hello, World!")

# Python Statements: A Statement is an instruction given to Python 
name = "Mehedi"
age = 25

print(name)
print(age)


# Indentation: Python uses indentation (spaces at the beginning of a line) to define a blog of code.
if age >= 18:
    print("You are an adult") # indention (4 spaces before print())


# Colon: A colon is used after statements that introduce a code block
if age >= 18:
    print("Adult")

# Comments: Comments are notes written for humans. PYthon ignores them when executing them program

# Variables: Variable store data
country = "Bangladeesh"

# Python is Case Sensitive 
# name = "Mehedi"
Name = "Rahim"
print(name)
print(Name)
# These are two different variable

# Strings: Text is written inside quotes 
language = "Python"
anotherLanguage = 'JavaScript'

# Numbers: Python supports integers and decimal numbers 
num1 = 25
num2 = 22.5

# Basic Operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(9 // 2) # Floor Division
print(10 % 2) # Modulus 
print(2 ** 2) # Power 

# Taking User Input 
userName = input("Enter your name: ")
print("Hello", userName)

# Basic if Structure 
makrs = 75
if makrs >= 80: 
    print("A+")
elif (makrs >= 70): 
    print("A")
else:
    print("Below A")

# Functions: A function is reusable block of code 
def greet():
    print("Hello, Mehedi")

greet()

# Importing Modules 
import math
print(math.sqrt(25))  