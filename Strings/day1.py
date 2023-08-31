# Day 1:
# Question: Write a function that takes a string as input and returns the reverse of that string.
# Example:
# Input: "hello"
# Output: "olleh"

# string - it is set of character
# it in enclosed by double quotes or single ("", '')
# ''' '''
# 'arsalan'
# 'arsalan123'
# '123'

# print(a[::-1]) #reversed string

# print(a[0:2:-1])
# print(a[0:4])

def reverse(mystring):
    return mystring[::-1]

a = reverse('arsalan')
print(a)
