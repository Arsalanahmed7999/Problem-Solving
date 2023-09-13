# Day2: Write a Python program that takes an integer input from the user and determines whether it's even or odd.

try:
    userInput = int(input('Enter any number: '))
    if(userInput % 2 == 1):
        print(f'The {userInput} is odd number')
    else:
        print(f'The {userInput} is even number')
except:
    print('Please enter a correct value')