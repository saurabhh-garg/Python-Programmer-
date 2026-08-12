# Q1: Your First Program
print("Hello, World! Welcome to Python.")

# Q2: Print a Poem
print("Twinkel, twinkle, little star,\nHow I wonder what you are!")

# Q3: Variables & Data Types
name = ("Saurabh")
age = ("19")
height = ("178.5")
student = True
print("The name of student is " + name + ". He is" + str(age) + "years old. " + "He is" + str(height) + "tall. " + "He is student: " + str(student) + ".")                  

# Q4: Typecasting Practice isse thoda detailed frae dene ke liye mene vlass type krwa kr str me change kiya h otherwise dirent print(int(num) + 10) bhi kr skte h
num = "45"
print("num:", type(num))
num_int = int(num)
num_int = num_int + 10
print("num_int:", num_int, type(num_int))

# Q5: Taking User Input
food = str(input("Enter your favourite food:"))
print("Wow! I also like", food)

# Q6: Simple Calculator
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print("sum:", a+b)
print("difference:", a-b)
print("product:", a*b)
print("quotient:", a/b)

# Q7: Escape Sequences
print("Harry said, \"Python is awesome!\"\nThis is on a new line.\nThis is a tab ->\t<- here")

# Q8: Operator Challenge
a = int(input("Enter your number:"))
print("square is:", a**2)
print("cube is:", a**3)