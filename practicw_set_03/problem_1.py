# 1. Basic String Operations:
# Create a string variable name with your full name. Print:
# The first character
# The last character
# The length of the string
name = input("Enter Your Full Name:")
print("first Character:", name[0])
print("Last Character:", name[-1])
print("Length:", len(name))


# Concatenate two strings: "Hello" and "World" with a space in between.
text = ['Hello', 'World']
new_text = " ".join(text)
print(new_text)