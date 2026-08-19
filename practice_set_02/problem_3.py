# 3. For Loops:
# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print (i)


# Print the multiplication table of a number (entered by user).
number = int(input("Enter the number: "))
for i in range (1,11):
    print(number, "X", i, "=", number*i)


# Calculate the sum of all numbers from 1 to 100 using a for loop.
sum = 0
for i in range(1, 101):
    print(i)
    sum += i
print("sum is: ", sum)


# Print the following pattern using a for loop:
# *
# **
# ***
# ****
for i in range(1, 5):
    print("*"*i)