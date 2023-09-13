# Question 11: Sum of Primes
# 10 -> 2, 3, 5, 7 ( 2 + 3 + 5 + 7 = 17)
# In the range of n return the sum of prime numbers 
# Prime are numbers which are divisible by 1 and the numbers itself, but 1 excluded, 1 has only 1 as the factor.
# 2, 3, 5, 7, 11, 13, 17, 19, 23,....

def is_prime(num):
    if(num<=1):
        return ('Please Enter the Number greater than 1')
    
    prime = True 
    #variable prime which is returning all the values of numbers are prime except for those who will go inside the if condition which is created inside the loop.

    for n in range(2, num):
        if(num % n == 0):
            prime = False
            break
    return prime
    
# print(is_prime(10)) #False
# print(is_prime(5)) #True

def sum_of_primes(numb):
    sumprimes = 0
    for n in range(2, numb + 1):
        if(is_prime(n)):
            sumprimes+=n
    return f'Sum of Primes: {sumprimes}'

print(sum_of_primes(10))
print(sum_of_primes(5))
print(sum_of_primes(7))
print(sum_of_primes(11))


