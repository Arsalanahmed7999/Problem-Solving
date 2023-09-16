# Question 16: Find the Second Largest Number
# Develop a Python function that finds and returns the second-largest number in a list of integers.

# list = [1, 2, 4, 5, 53, 2432, 100, 102] #output - 102

def second_largest_num(nums):
    nums.sort()
    if(len(nums) == 0 or len(nums)==1):
        return -1
    else:
        return nums[len(nums) - 2]


print(second_largest_num([10312, 2, 4, 5, 53, 2432, 100, 102]))
print(second_largest_num([]))
print(second_largest_num([1]))
print(second_largest_num([4,14]))