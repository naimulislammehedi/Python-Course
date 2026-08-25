# 🎯 Goal
# Create a program that takes a student's score and determines their grade.

# Rules
    # 80–100 -> A
    # 70–79	-> B
    # 60–69	-> C
    # 50–59	-> D
    # Below 50	-> F

# Hint: You'll need:
    # if
    # elif
    # elif
    # elif
    # else
# Don't worry about handling invalid scores yet. Just assume the score is between 0 and 100.

score = 75

if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")