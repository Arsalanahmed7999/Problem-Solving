# Question 15: Check for Harshad Number
# Implement a Python function that checks if a given integer is a Harshad number. A Harshad number (Niven number) is an integer that is divisible by the sum of its digits.
# num = 123
# sum_of_digits = 1 + 2 + 3 = 6
# check whether this num is divisible by sum of its digits.
# 123 % 6 != 0, False
# Num = 12, Sum = 3
# 12 % 3 == 0, True

def harshad_number(num): #Example: num = 123 
    original_num = num
    summ = 0
    while num > 0:
        digit = num % 10
        summ+=digit
        num = int(num / 10) # value as 12.3 -> 12, value as 1.2 -> 1
    # return num % summ == 0
    return original_num % summ == 0

print(harshad_number(123))
print(harshad_number(12)) 

# print(123 % 6 == 0) 
