# Day 7:
# Write a Python function to find the index of the last occurrence of a specific element in a list.
# Example:
# Input: [5, 10, 15, 10], Element: 10
# Output: 3

def last_occurance(mylist, element):
    for i in range(len(mylist) - 1 , -1, -1):
        if(mylist[i] == element):
            return (i)
    return -1

print(last_occurance([5, 10, 15, 10], 10))
print(last_occurance([5, 10, 15, 10], 1))
print(last_occurance([5, 10, 15, 10], 5))