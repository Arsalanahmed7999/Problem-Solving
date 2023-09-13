# Prime Number Check:
# Develop a program that checks whether a given integer is a prime number or not.

# primenumber are numbers which are only divisible by 1 and the number itself.
# 1 is not a prime number 
# 2, 3, 5, 7.. are prime numbers 
# factors of 2 = [1, 2]
# factors of 3 = [1, 3]
# factors of 5 = [1, 5]
# factors of 4 = [1,2,4] #Not a prime Number
# num = 10 [3, 4, 5, 6, 7, 8 , 9, 10]
# square root of 10 will not be a interger 
# I used int function to convert it in integer, because range function takes numbers which are intergers not float value

def check_prime(num):
    if(num<=1):
        return ('Please Enter a number greater than 1')
    elif(num == 2):
        return True
    # for n in range(3, int(num ** 0.5) + 1):
    #     if(num % n == 0):
    #         return False
    # return True
    # factors = []
    # for n in range(2, num + 1):
    #     if(num % n == 0):
    #         factors.append(n)
    # return (len(factors) == 1)
    prime = True
    for n in range(2, num):
        if(num % n == 0):
            prime = False
            break
        # if n = 2 it will be not going inside the if condition and directly exiting,
        # if n = 3 it will be not going inside the if condition and directly exiting,
        # if n = 4 it will be not going inside the if condition and directly exiting,
    return prime

    
print(check_prime(0))
print(check_prime(5))
print(check_prime(41))
print(check_prime(10))
print(check_prime(1319299131291))
      