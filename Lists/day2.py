# Question: Write a Python function to calculate the sum of all elements in a list of numbers.
# Example:
# Input: [2, 5, 7, 10]
# Output: 24

def sumOfNums(nums):
    # return sum(nums)
    summ = 0 #initial sum
    for num in nums:
        summ = summ + num
        # first iteration
        # summ = 0 + 2 = 2
        # second iteration
        # summ = 2 + 5 = 7
        # third iteration
        # summ = 7 + 7 = 14
        # fourth iteration
        # summ = 14 + 10 = 24
        # Exiting the loop
    return summ


    
print(sumOfNums([2,5,7,10])) #24
print(sumOfNums([10, 3, 2])) #15



