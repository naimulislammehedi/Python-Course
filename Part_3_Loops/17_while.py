# A while loop is used to repeatedly execute a block of code as long as a condition is True.

count = 1 

while count <= 5:
    print(count)
    count += 1

# A while loop needs something that eventually makes its condition False.


# Using a while Loop with User Input
password = ""

while password != "1234":
    password = input("Enter password: ")

print("Acess granted!")
