# GCD:
# Implement functions to find the Greatest Common Divisor (GCD).
# HCF = Highest Common Factor

# num1 = 10
# num2 = 20
# factorsOfNum1 = [1, 2, 5, 10]
# factorsOfNum2 = [1, 2, 4, 5, 10, 20]

# commonFactors = [1, 2, 5, 10]
# GCD = 10

def hcf(num1, num2):
    max_num = max(num1, num2)
    commonFactors = []
    for num in range(1, max_num + 1):
        if((num1 % num == 0) and (num2 % num == 0)):
            commonFactors.append(num)
    # return f'HCF: {max(commonFactors)}'
    # Alternate way
    return f'HCF: {commonFactors[-1]}'

print(hcf(10, 20)) 
print(hcf(30, 43)) 
