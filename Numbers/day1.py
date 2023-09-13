# Day1: Find the sum of odd numbers to n range

# range = 100
# 1,3,5,7,9,11...99
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + .... 
# If the number is even it is divisible by 2 , number 40 / 2 (remainder = 0), %
# any even number if we divide it by 2, number % 2 == 0
# If the number is odd it is not divisible by 2 
# If the number is divided by 2 and the remainder is 1 then it is odd value and if it is 0 then it is an even number
def oddsum(n):
    sumoofodd = 0
    for num in range(0, n + 1):
        if(num % 2 == 1):
            sumoofodd = sumoofodd + num
    return sumoofodd



print(oddsum(4)) # 1 + 3 
print(oddsum(10)) # 1 + 3 + 5 + 7 + 9
print(oddsum(100))
# a = 40 
# b = 41
# print(a % 2) # even number - remainder will be 0
# print(b % 2) # odd number - remainder will be 1



