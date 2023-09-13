# Question: Given a sentence, write a function to capitalize the first letter of each word in the sentence.
# Example:
# Input: "this is a sample sentence."
# Output: "This Is A Sample Sentence."

def capitilize(mystr):
    mylist = mystr.split(' ') #converting the into a list
    temp = [] #puting the word in this list
    for word in mylist:
        # temp.append(word[0].upper() + word[1:]) #1 this -> ['T' + 'his'], #2 is -> ['I' + 's'], #3 'a' -> ['A'], #4 'sample' -> ['S' + 'ample] #5....
        temp.append(word.capitalize())

    # return temp #this valus is still not our answer because is a list
    ans = " ".join(temp)
    return ans



print(capitilize('this is a sample sentence'))

