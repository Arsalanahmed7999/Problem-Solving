# Day 9: List Filtering
# 9. Given a list of numbers, write a Python function that filters out all even numbers and returns a new list containing only the odd numbers.

nums = [1,2,3,4,5]
newnums = [1, 3, 5]

def is_odd(num):
    if(num % 2 == 1):
        return True
    
def list_filtering(nums):
    odd_nums = []
    for n in nums:
        if(is_odd(n)):
            odd_nums.append(n)
    return odd_nums

print(list_filtering([1,2,3,4,5]))