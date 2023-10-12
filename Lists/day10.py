# Day 10:
# List Flattening:
# Write a Python function to flatten a nested list, turning it into a one-dimensional list.
# For example, if the input is [[1, 2], [3, 4, 5], [6]], the function should return [1, 2, 3, 4, 5, 6].

def list_filtering(myList):
    newList = []
    for elements in myList:
        for items in elements:
            # print(items)
            newList.append(items)
        # print(elements)
    return newList

print(list_filtering([[1,2], [3,4,5], [6]]))
print(list_filtering([[1,2], ["Arsalan", "Ahmed"], [6]]))

# First interation of outer loop (running it for elements)
# [1, 2]
# First iteration of inner loop (running it for items)
# 1
# Second iteration of inner loop (running it for items)
# 2
# It will exit the inner loop of first iteration



# Second interation of outer loop (running it for elements)
# [3, 4, 5]
# First iteration of inner loop (running it for items)
# 3
# Second iteration of inner loop (running it for items)
# 4
# Third iteration of inner loop (running it for items)
# 5
# It will exit the inner loop of second iteration


# Third interation of outer loop (running it for elements)
# [6]
# First iteration of inner loop (running it for items)
# 6
# It will exit the inner loop of third iteration


# It will exit the outer loop and it will eventually and finally return me the newlist