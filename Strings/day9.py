# Substring Search
# Write a Python function that checks if a given substring exists within a larger string.
# Input-
# main_string = "Hello, World!"
# substring1 = "World"
# substring2 = "Python"
# Output-
# True
# False

def checkSubstring(mainString, substring):
    return substring in mainString

print(checkSubstring("Hello, World!", "World"))
print(checkSubstring("Hello, World!", "Python"))