# Write a function that takes a string as input and returns the number of words in the string.
# Input: "Hello, how are you?"
# Output: 4

def numberOfWord(sentence):
    mylist = sentence.split(' ')
    return len(mylist)

print(numberOfWord("Hello, how are you?"))

