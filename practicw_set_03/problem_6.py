# 6. Bonus Questions:

# Write a program that counts how many vowels are in a given string.
sentence = "Coding in Python is fun" 
vowels = ['a', 'e', 'i', 'o', 'u']
sum = 0
for char in sentence:
    if (char in vowels):
        sum += 1
print(f"the sum of vowels in sentence is {sum}")



# Take a user input string and check if it is a palindrome (same forwards and
# backwards).
string = "Hello"
if(string == string[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")