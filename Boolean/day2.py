# Day 2: Palindrome Checker
#.Write a Python function that checks if a given string is a palindrome (reads the same forwards and backwards) and returns True if it is, False otherwise.

# aba - True 
# abc = False


def palindrome(mystr):
    # if(mystr == mystr[::-1]):
    #     return True
    # else:
    #     return False
    return mystr == mystr[::-1]


print(palindrome('abaa'))
print(palindrome('aba'))
