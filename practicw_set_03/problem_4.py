# 4. String Formatting and f-Strings:

# Using format() , create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
template = "My name is {} and I am {} years old."
a = "John"
a1 = 25

print(template.format(a, a1))

# Do the same using f-strings.
print(f"My name is {a} and I am {a1} years old.")