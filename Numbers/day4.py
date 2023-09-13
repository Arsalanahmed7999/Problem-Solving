# Day4: Sum of Even numbers
# range = 10
# even number = 2, 4, 6, 8, 10
# sum of all of these numbers = 2 + 4 + 6 + 8 + 10 -> (30)
def evenSum(n):
    sumOfEvenNums = 0 #(0 + 2, 2 + 4, 4 + 6, 6 + 8, 8 + 10)
    # sumOfEvenNums+=2
    # sumOfEvenNums+=4
    # sumOfEvenNums+=6
    # sumOfEvenNums+=8
    # sumOfEvenNums+=10
    # sumOfEvenNums+=12
    # sumOfEvenNums+=14
    # sumOfEvenNums+=16
    # print(sumOfEvenNums)

    for num in range(0, n + 1):
        if(num % 2 == 0):
            sumOfEvenNums+=num
    print(sumOfEvenNums)


# evenSum(10)
evenSum(100)

# To check a num is even or odd
# % operator is used to give the remainder
# if num % 2 == 1 then it is a odd number
# if num % 2 == 0 then it is a even number

# a = 40
# print(a % 2)

# a = 41

# print(a % 2)