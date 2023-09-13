# Question: Write a function that takes a string as input and returns the first non-repeated character in the string. If there are no non-repeated characters, return None.
# Example:
# Input: "programming" Non Repeated
# Output: "p"
# Input: "pprroo" Repeated string
# Output: "None"


# a = 'Arsalllan'
# print(len(a))
# print(a.count('A'))
# print(a.count('l'))

# Count is an inbuilt function which counts the number of occ. of a charter inside a string

# We will counting the number of character occurances and then we will be checking their len = 1

def non_repreated_character(mystring):
    temp = "" #Empty string
    for char in mystring:
        if(mystring.count(char) == 1):
            temp = temp + char 
            # temp = "" + "p"
            # temp = "p" + "o"
            # temp = "po" + "a"
            # temp = "poa" + "i"
            # temp = "poai" + "n"
            # After this it will exit the loop
    if(len(temp) == 0):
        return None
    return temp[0] #and then it will return us this value

print(non_repreated_character("programming"))
print(non_repreated_character("pprroo"))


