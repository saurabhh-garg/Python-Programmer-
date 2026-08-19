# 1. If-Else Conditional Statements:

# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
number = int(input("Enter the number:"))
print(number)
if number > 0:
    print("The number is Positive!")
elif number < 0:
    print("The number is Negative!")
else:
    print("The number is Zero!")


# # Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter Your Age:"))
if age >= 18:
    print("Your are Eligible for Voting!")
else:
    print("Your are NOT Eligible for Voting!")


# Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.
NUMBER = int(input("Enter the number"))
NUMBER = NUMBER % 2
if NUMBER == 0:
    print("even")
else:
    print("odd")
