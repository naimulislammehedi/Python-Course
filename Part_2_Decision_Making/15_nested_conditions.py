# Nested Conditions
# A nested condition means placing one if statement inside another if statement.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

## Another example 
username = "Mehedi"
password = "1234"

if username ==  "Mehedi":
    if password == "1234":
        print("Login successful")


# Nested if_else 
if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID required")
else:
    print("You are too young")