# The range() function generates a sequence of numbers. It is most commonly used with a for loop. 
# Think of range() as:
    # “Generate numbers from here to there, with this step.”

for number in range(5):
    print(number)

print("===================")

# range(start, stop)
for number in range(1, 6):
    print(number)

print("===================")

# range(start, stop, step)
for number in range (2, 11, 2):
    print(number)

print("===================")

# Counting by 3
for number in range(3, 16, 3):
    print(number)

print("===================")

# Counting Backward
for number in range (10, 0, -1):
    print(number)
    
print("===================")

# range() with Negative Numbers
for number in range(-5, 1):
    print(number)

print("===================")

# Print 1–10
for i in range(1, 11):
    print(i)