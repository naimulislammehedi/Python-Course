# Identity Operators
# These compare whether two variables refer to the same object in memory.

a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)