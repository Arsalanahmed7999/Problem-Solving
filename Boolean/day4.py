# Day 4:
# String Suffix Checker: Write a Python function that checks if a given string str1 is a suffix of another string str2 and returns True if it is, False otherwise.

# Input : Mango, go
# Output: True
# Input : Mango, ar
# Output: False

def suffix_checker(str1, str2):
    if(str1.endswith(str2)):
        return True
    else:
        return False

print(suffix_checker('Mango', 'go')) #True
print(suffix_checker('Mango', 'ar')) #False

# a = 'Mango'
# print('Mango'.endswith('Ngo'))