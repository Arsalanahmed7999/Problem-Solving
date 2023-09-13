# Question: Write a function that takes a string as input and returns True if it is a palindrome (reads the same backward as forward), otherwise returns False.
# Example:
# Input: "racecar"
# Output: True

def palindrome(mystr):
    forward = mystr
    reverse = mystr[::-1]
    return forward == reverse

print(palindrome("racecar"))
print(palindrome("ahmed"))
