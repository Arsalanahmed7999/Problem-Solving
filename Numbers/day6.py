# FizzBuzz:
# Create a program that prints numbers from 1 to 100, but for multiples of 3, print "Fizz" instead, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

def fizzbuuz(n):
    for nums in range(1, n + 1):
        if(nums % 3 == 0 and nums % 5 == 0):
            print(f"{nums}: FizzBuzz")
        elif(nums % 5 == 0):
            print(f"{nums}: Buzz")
        elif(nums % 3 == 0):
            print(f"{nums}: Fizz")
        else:
            print(f"{nums}")
fizzbuuz(100)