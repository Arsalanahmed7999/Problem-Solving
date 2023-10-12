# Question 1: Max Value in a list
# Write a Python function to find the maximum value in a list of numbers.
# Example:
# Input: [5, 10, 3, 8, 15]
# Output: 15

def max_value(l1):
    # return max(l1)
    l1.sort()
    return l1[-1]
    # maxVal = 0
    # for num in l1:
    #     if(maxVal<num):
    #         maxVal = num
    # return maxVal

print(max_value([5, 10, 3, 15, 8, -100]))
print(max_value([-100, -10, -6, -2]))