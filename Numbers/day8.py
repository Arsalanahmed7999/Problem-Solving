# Day 8: 
# LCM - Implement functions to find the Least Common Multiple.

# num1 = 10
# num2 = 20

# multiplesOf10 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
# multiplesOf20 = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

# commonMultiples = [20, 40, 60, 80, 100, 120, 140]
# lcm = 20

def lcm(num1, num2):
    commonMultiples = []
    rangeNum = num1 * num2 
    for num in range(1, rangeNum + 1):
        # I will be putting a condition, saying the if there is any num which is divisible by both num1 and num2
        if(num % num1 == 0 and num % num2 == 0):
            commonMultiples.append(num)
    # return f'LCM: {min(commonMultiples)}'
    # Alternate Way
    return f'LCM: {(commonMultiples[0])}'
    

print(lcm(10,20))
print(lcm(15,5))
print(lcm(7,31))

