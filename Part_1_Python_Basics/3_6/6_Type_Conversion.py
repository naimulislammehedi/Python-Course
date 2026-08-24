# Python Type Conversion: type conversion means changing a value from one data type to another 
age = "25"
print(type(age))
age = int(age)
print(type(age))

# a very common example is input()
age = input("Enter your age: ")
print(type(age))
age = int(age)
print(age + 5)

# float() - convert to float 
x = float("25")
print(x)

# str() - convert to string 
age = 25 
age = str(age)
print("My age is " + str(age))

# bool() - Convert to Boolean 
print(bool(1))
print(bool(0))

# example with inp() 
# Suppose you're creating a simple shopping calculator 
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(total)