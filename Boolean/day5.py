# Day 5:
# String Prefix Checker: Write a Python function that checks if a given string str1 is a prefix of another string str2 and returns True if it is, False otherwise.

# Input : Mango, Ma
# Output: True
# Input : Mango, Mr
# Output: False

def prefix_checker(str1, str2):
    # if(str1.startswith(str2)):
    #     return True
    # else:
    #     return False
    return str1.startswith(str2)

print(prefix_checker('Mango', 'Ma')) #True
print(prefix_checker('Mango', 'ma')) #False
print(prefix_checker('Mango', 'Mr')) #False
 
