# Day 6: Find First Index
# Question: Write a Python function to find the index of the first occurrence of a specific element in a list.
# Example:
# Input: [5, 10, 15, 10], Element: 10
# Output: 1

def find_first_index(l, element):
    for elem in l:
        if(elem == element):
            return (f'The index of the first occurence of {elem} inside a list {l} is {l.index(elem)}')
    return f'{element} is not present inside the list {l}'

print(find_first_index([5, 10, 15, 10], 10))
print(find_first_index([5, 10, 15, 10], 2))




