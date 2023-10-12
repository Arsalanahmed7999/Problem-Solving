# Day 7: List Intersection
# 7. Create a Python function that takes two lists as input and returns True if they have at least one common element and False otherwise.

# list1 = [1, 'Two', 3, 4, 5]
# list2 = [6, 7, 8 ,9, 1]
# # True

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8 ,9, 10]

# # False

def list_intersection(list1, list2):
    for elements in list1:
        if(elements in list2):
            return True
    return False

print(list_intersection(['two' ,3 ,4 ,5], [6, 7, 8, 9, 'two']))
print(list_intersection([1,2,3,4,5], [6, 7, 8, 9, 10, 5]))
print(list_intersection([1,2,3,4,5, [1, 2,3]], [6, 7, 8, 9, 10, [1,2,3]]))