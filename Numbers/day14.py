# Question 14: Reverse an Integer
# Create a Python function that takes an integer as input and returns the integer with its digits reversed. For example, input 12345 should return 54321.

def reverse_integer(num):
    # Type conversion logic
    # return (int(str(num)[::-1]))

    reverse_n = 0
    while num >0:
        digit = num % 10 #(1st Iteration digit = 5)
        reverse_n = reverse_n * 10 + digit
        # num = num // 10
        num = int(num / 10)
    return reverse_n

print(reverse_integer(12345))
print(reverse_integer(950312))

# I will adding the remainder of the number to my reverse_n

# print(12345 % 10)

# 1st iteration reverse_n = 5
# 2nd iteration reverse_n = 50
# 3rd iteration reverse_n = 500
# 4th iteration reverse_n = 5000
# 5th iteration reverse_n = 50000

# print(12345 // 10) #it divides the value and give you an integer value
# print(int(12345 / 10)) #it divides the value and give you an integer value

# 1st iteration reverse_n = 0 * 10 + 5 = 5 
# 2nd iteration reverse_n = 5 * 10 + 4 = 54
# 3rd iteration reverse_n = 54 * 10 + 3 = 543 
# 4th iteration reverse_n = 543 * 10 + 2 = 5432
# 5th iteration reverse_n = 5432* 10 + 1 = 54321
