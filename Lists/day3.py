# Day 3:
# Write a Python function to check if a given element exists in a list.
# Example:
# Input: [3, 7, 9, 12], Element: 7
# Output: True

def check_given_element(myList, element):
    # in keyword
    # if(element in myList):
    #     return True
    # else:
    #     return False
    for item in myList:
        if(item == element):
            return True
    return False

print(check_given_element([3, 7, 9, 12], 7))
print(check_given_element([3, 7, 9, 12], 10))


