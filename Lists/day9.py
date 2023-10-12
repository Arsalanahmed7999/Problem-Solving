# Day 9:
# Nested List Sum
# Write a Python function called nested_list_sum that takes a nested list of numbers as input and returns the sum of all the numbers in the nested list. Assume that the nested list contains only integers.
# Example:
# Input : [[1, 2, 3], [4, 5], [6]]
# Output: 21

def nested_list_sum(nums):
    sum = 0
    for i in range(len(nums)):
        for j in nums[i]:
            sum+=(j)
    return sum

print(nested_list_sum( [ [1, 2, 3], [4, 5], [6] ] ))

# first iteration for i
# i = 0 [1, 2, 3]
# for first iteration for j
# sum = sum  + j
# sum = 0  + 1
# for second iteration for j
# sum = sum  + j
# sum = 1  + 2
# for third iteration for j
# sum = sum  + j
# sum = 3  + 3

# Now it exit the first iteration i
# sum = 6


# second iteration for i
# i = 1 [4, 5]

# for first iteration for j
# sum = sum  + j
# sum = 6  + 4
# for second iteration for j
# sum = sum  + j
# sum = 10  + 5

# Now it again exit the ith loop with sum = 15

# third iteration for i
# i = 2 [6]
# for first iteration for j
# sum = sum  + j
# sum = 15  + 6

# And then it will finally exit every loop and return a sum value. with sum = 21

