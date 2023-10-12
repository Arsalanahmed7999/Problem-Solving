# Create a dictionary that contains the squares of numbers from 1 to 5.
# Create a dictionary that contains the length of each word in a list of words: ["apple", "banana", "cherry", "date"].
# Create a dictionary that contains the frequency of each character in a given string.

# For example, given the string "hello", the dictionary should be {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

# squares = {
#     1 : 1,
#     2 : 4,
#     3 : 9,
#     4 : 16,
#     5 : 25
# }
squares = {
    num : num ** 2 for num in range(1,6)
}
print(squares[2])

fruits = ["apple", "banana", "cherry", "date"]
listLen = {
    fruit : len(fruit) for fruit in fruits
}

string1 = 'hello'

# charFreq = {
#     char: string1.count(char) for char in string1
# }
# print(charFreq['h'])

charFreq = {}

for char in string1:
    if(char in charFreq):
        charFreq[char]+=1
    else:
        charFreq[char] = 1

print(charFreq['h'])
