# Day 2:
# Question: Given a string, write a function to count the number of vowels (a, e, i, o, u) in the string.
# Example:
# Input: "programming"
# Output: 3

def count_vowels(mystr):
    count = 0 #this will be counting the number of vowels
    for letter in mystr:
        if(letter == 'a' or letter == 'e' or letter=='i' or letter =='o' or letter == 'u'):
            count+=1 #(0->1->2->3)
    return f'Vowels count: {count}'
print(count_vowels('programming'))

