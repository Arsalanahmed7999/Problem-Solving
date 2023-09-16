# Question 13: Largest Digit
# Write a Python function that finds the largest digit in a given integer.
# Input : 123219
# Output : 9

def largest_digit(num):
    myNum = 0 #Created this variable to compare it with each individual digit inside a num
    num = str(num) #So that it can iterate through
    for i in num:
        if(int(i) > myNum): #1st iteration (3 > 0), myNum = 3, 2nd iteration (1 < 3), 3rd interation (2 < 3), 4th iteration (4>3, myNum = 4)
            myNum = int(i)
    return myNum


print(largest_digit(3124))



