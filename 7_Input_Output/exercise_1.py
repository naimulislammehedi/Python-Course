# 🧩 Exercise 1: Personal Information
# Write a Python program that:
# Takes the user's name as input.
# Takes the user's age as input.
# Takes the user's country as input.
# Prints all three pieces of information in a clear format.

# Expected interaction
# Enter your name: Mehedi
# Enter your age: 25
# Enter your country: Bangladesh

# --- Personal Information ---
# Name: Mehedi
# Age: 25
# Country: Bangladesh

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print("--- Personal Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")