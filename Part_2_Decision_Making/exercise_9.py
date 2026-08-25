# Write a program with:
# age = 20
# has_ticket = True

# Rules:
    # If age >= 18
    # If has_ticket is True → print "You can enter."
    # Otherwise → print "You need a ticket."
    # If under 18 → print "You are too young."

age = 20
has_ticket = True

if age >= 18: 
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket.")
else:
    print("You are too young.")