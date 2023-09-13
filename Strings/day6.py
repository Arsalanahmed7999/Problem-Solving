# Question: Write a function that takes a string as input and returns the longest word in the string.
# Example:
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "quick"

def longestWord(mystr):

    temp = [] #list to get all the words from the string
    mystr = mystr.split(' ') #converting list into string #['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

    for word in mystr:
        temp.append(len(word)) # I am using the length function and appending the lengths of the word inside the mystr list, [3, 5, 5, 3, 5, 4, 3, 4, 3]
    longestLength = max(temp) # I am checking for the longest length of any word inside temp list
    # return longestLength, #longestlength = 5, 3

    for word in mystr:
        if(len(word)==longestLength): #[3, 4, 5, 3, 5, 4, 3, 4, 3], 3 < 5, 4> 5, 5 == 5
            return word
        

print(longestWord("The quic brown fox jumps over the lazy dog"))
print(longestWord("Th dog"))
