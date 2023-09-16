# Day 18: Armstrong Number

# Implement a Python function that checks if a given integer is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
# Input: 153 
# Output: True
# Input: 32
# Output: False

# sumofdigits = (1^3) + (5^3) + (3^3) = 1 + 125 + 27 = 153
# sumofdigits = (3^2) + (2^2)  = 9 + 4 = 13

def armstrong_number(num):
    originalNum = num
    lenOfNum = len(str(originalNum)) 
    #this variable is the power of each individual digit in the number
    summ = 0
    while num > 0:
        digit = num % 10 #153 % 10 = 3
        summ+=(digit**lenOfNum)
        num = int(num / 10) # (153 / 10 = 15.3)
    return summ == originalNum

print(armstrong_number(153)) #True
print(armstrong_number(32)) #False
