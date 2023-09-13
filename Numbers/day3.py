# Day 3: Write a function to calculate the factorial of a non-negative integer.


# Factorial = 10 -> 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
# Factorial of 0 = 1
# Factorial of 1 = 1

def factorial(num):
    if(num < 0):
        return('Please enter a non-negative integer')
    elif(num == 0 or num == 1):
        return 1
    else:
        fac = 1
        for n in range(2, num + 1):
            fac = fac * n 
            # fac = 1 * 2, fac = 2 * 3, fac = 6 * 4, fac = 24 * 5, fac = 120 * 6.....
        return f'Factorial of {num}: {fac}'


a = factorial(10)
print(a)
a = factorial(5)
print(a)
a = factorial(2)
print(a)
a = factorial(3)
print(a)
a = factorial(6)
print(a)