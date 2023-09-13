# Question 10: Prime Factorization
# Develop a Python function that finds and returns the prime factors of a given number.


# prime_number are numbers which are divisible by 1 nad the unmber itself, including 2, 3, 5, 7, 11, 13..
# factors are numbers which can divide any particular number completely, giving the remainder as 0.
# factors of 10 = [1, 2, 5, 10]
# prime factors of 10 = [2, 5]
# 100, 200

# Function to check the prime number
def is_prime(num):
    if(num<=1):
        return('Please Enter a Number greater than 1')
    prime = True
    for n in range(2, num):
        if(num % n == 0):
            prime = False
            break
    return prime

# print(is_prime(10)) #False
# print(is_prime(2)) #True

# Creating a function to calculate the prime factorization
def prime_factorization(numb):
    primeactors = [] #Empty list, the factor will be appended inside this

    for n in range(2, numb + 1):
        if is_prime(n) and numb % n == 0:
            primeactors.append(n)
    return f'PrimeFactors of {numb}: {primeactors}'


print(prime_factorization(10))
print(prime_factorization(100))
print(prime_factorization(5))
print(prime_factorization(542))