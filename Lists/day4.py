# Day 4: Count Occurrence 
# Question: Write a Python function to count the occurrences of a specific element in a list.
# Example:
# Input: [2, 5, 3, 2, 7, 2], Element: 2
# Output: 3

def count_occurrence(l1, element):
    # return l1.count(element)
    cnt = 0
    for elem in l1:
        if(elem == element):
            cnt+=1
    return cnt

print(count_occurrence([2, 5, 3, 2, 7, 2], 2))
print(count_occurrence([2, 5, 3, 2, 7, 2], 7))
print(count_occurrence([2, 5, 3, 2, 7, 2], 10))
