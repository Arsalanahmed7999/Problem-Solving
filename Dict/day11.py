# Write a function that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the frequencies of those words. Ignore punctuation and consider words in a case-insensitive manner.
# import string
def func(string):
    # string = string.translate(str.maketrans("", "", string.punctuation))
    # return string
    string = string.split(' ')
    mydict = {}
    for word in string:
        if(word.lower() in mydict):
            mydict[word.lower()]+=1
        else:
            mydict[word.lower()] = 1
    return mydict
a = func('I am Arsalan')
print(a)
a = func('I am Arsalan, Arsalan')
print(a)

