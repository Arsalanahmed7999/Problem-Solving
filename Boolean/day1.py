# Day 1:
# Substring Checker: Write a Python function that checks if a given substring exists in a larger string and returns True if it's found, False otherwise.

# boolean = True or False

def substring_checker(largerstr, substr):
    if(substr in largerstr):
        return True
    else:
        return False
    
print(substring_checker('Hello World', 'World'))
print(substring_checker('Hello World', 'Python'))


# a = 5
# b = 10
# print(type(a < b))
# print(a > b)