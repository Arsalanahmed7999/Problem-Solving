# Day 6: User Authentication
#  Write a Python program that simulates user authentication. It should ask the user for a username and password, and if the provided credentials match predefined values, it should return True for successful authentication, otherwise False.

email = input('Enter your email: \n') 
password = input('Enter your password: \n')

def user_authentication(yourpassword, youremail):
    if(yourpassword == password and youremail == email):
        return True
    else:
        return False

youremail = input('Verify your email: \n') 
yourpassword = input('Verify your password: \n')

print(user_authentication(yourpassword, youremail))
# print(user_authentication(yourpassword, youremail))

