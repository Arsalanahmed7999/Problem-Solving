# Day 5: Removing specific element
# Question: Write a Python function to remove all occurrences of a specific element from a list.
# Example:
# Input: [1, 2, 3, 2, 4, 2], Element: 2
# Output: [1, 3, 4]

def removing_specific_element(l, element):

    for elem in l:
        if(elem == element):
            l.remove(element)
    return l

print(removing_specific_element([1, 2, 3, 2, 4, 2], 2))


