# Day 8:
# Lucky Number Checker: Write a Python function that checks if a given number is a "lucky number." A lucky number is a number that contains only the digits 4 and 7.

# num = 47 #luckynumber
# num = 407 #not a lucky number
# num = 47777 #luckynumber


def lucky_number(numb):
    temp = ""
    numb = str(numb)
    for digit in numb:
        if(int(digit) == 4 or int(digit)==7):
            temp+=digit
    
    if(len(temp) == len(numb)):
        return True
    else:
        return False
    # return len(numb), len(temp)

print(lucky_number(4747771230127)) # False
print(lucky_number(474747777)) # True
