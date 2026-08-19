# 4. While Loops:
# Print numbers from 1 to 10 using a while loop.
i = 0
while i<=10:
    print(i)
    i += 1


# Write a program that keeps asking the user to enter a password until they enter the correct one.
password = 231005
Enter_Password = int(input("Enter the Password: "))
while (Enter_Password != password):
    Enter_Password = int(input("Wrong Password! Try Again: "))

print("Login Successful")


# Use a while loop to reverse a given number (e.g., 123 → 321).
num = 23456
print(int(str(num)[::-1]))