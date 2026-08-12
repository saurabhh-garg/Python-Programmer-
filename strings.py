name = input("Enter Your Username: ")

print("Username Analyzer working.....")

# first character
# last character
# third character
print("first character:", name[0])
print("last character:", name[-1])
print("third character:", name[2])

# First 4 characters
# Last 4 characters
# Username ko reverse karo
print("first four character:", name[0:4])
print("last four character:", name[-4:])
print("reverse character:", name[::-1])

# .upper()
# .lower()
# .replace()
# .count()
print("Uppercase:", name.upper())
print("lowercase:", name.lower())
print("replace:", name.replace("a", "@"))
print("cout of a:", name.count("a"))


