# Day 20 - Check a leap year
# To check for a leap year, year should be divisible by 4 but it should not a century year except it is divisible by 400
# Input: 2000
# Output: Leap Year
# Input: 2024
# Output: Leap Year
# Input: 2122
# Output: Not a Leap Year

def check_leap_year(year):
    # if 2000 % 4 == 0 #True for a leap year
    # if 2000 % 100 == 0 #False for a leap year
    # except if 2000 % 400 == 0 #True for a leap year

    if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(check_leap_year(2000)) #leap year
print(check_leap_year(2100)) # not a leap year
print(check_leap_year(2024)) # leap year
print(check_leap_year(2023)) # not a leap year

# print(2100 % 4)