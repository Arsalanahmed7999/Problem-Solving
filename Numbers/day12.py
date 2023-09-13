# Question 12: Sum of Digits

# Example num = 123 = 6
def sum_of_digits(num):
    s = 0 #sum of digits
    # for i in range(0, num):
    #     digits = num % 10
    #     s+=digits
    #     # num = num // 10
    #     num = int(num / 10)
    # print(s)
    # first iteration (num = 123)
    # s = remainder of 123 % 10 = 3
    # s + 3
    # s = 3
    
    # second iteration (num = 12)
    # s = remainder of 12 % 10 = 2
    # s + 3 + 2
    # s = 5

    # third iteration (num = 12//10 = 1)
    # s = remainder of 1 % 10 = 1
    # s + 3 + 2 + 1
    # s = 6

    # Alternate approach
    # num = str(num)
    # for i in num:
    #     s+=int(i)
    # return s
    


print(sum_of_digits(123))
# num = 123 
# print(num % 10) # we are taking out the remainder
# print(num // 10) # we are taking out the floor division
# 12.3  = 12
# print(119 // 10) # we are taking out the floor division
# 11.9 if you convert this into integer 11
# print(int(11.9))
