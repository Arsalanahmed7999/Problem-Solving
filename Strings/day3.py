# Write a function that takes two strings as input and returns True if one string is an anagram of the other, otherwise returns False.

# Hint: Another string that contains the same characters, only the order of characters can be different
# Example:
# Input: "listen", "silent" #Anagram 
# Input: "listen", "silennt" #Not Anagram
# Output: True

def anagram(string1, string2):
    l1 = list(string1) #['l','i', 's', 't', 'e', 'n']
    l2 = list(string2) #['s', 'i', 'l', 'e', 'n', 't']
    l1.sort() # ['e', 'i', 'l', 'n', 's', 't']
    l2.sort() # ['e', 'i', 'l', 'n', 's', 't']
    s1 = "".join(l1) #converting the list into string
    s2 = "".join(l2) #converting the list into string
    return s1 == s2

print(anagram('listen', 'silent'))
print(anagram('listen', 'silent'))
print(anagram('anagram', 'gramana'))
print(anagram('anaaagram', 'ggramana'))