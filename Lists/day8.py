# Day 8:
# Write a Python function to reverse a list.
# Example:
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]

def reverse_list(mylist):
    # return mylist[::-1]
    newList = []
    for i in range(len(mylist)-1, -1, -1):
        # print(i) #this is printing indexing
        newList.append(mylist[i])
    return newList


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([10, 19, 18, 201]))