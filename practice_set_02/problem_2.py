# 2. Match Case Statements:

# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case .
day_num = int(input("Enter the Day Number:"))
match day_num:
    case 1:
        print("Sunday!")
    case 2:
        print("Monday!")
    case 3:
        print("Tuesday!")
    case 4:
        print("Wednesday!")
    case 5:
        print("Thursday!")
    case 6:
        print("Friay!")
    case 7:
        print("Saturday!")    


# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .
 
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter SECOND Number:"))

operation = input("Choose Your operation:")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)

