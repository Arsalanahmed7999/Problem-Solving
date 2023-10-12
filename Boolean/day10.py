# Day 10: Password Validation
# 10. Create a Python function that checks if a user-provided password meets the following criteria:
# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one digit.
# Contains at least one special character (e.g., @, #, $).

def password_validation(password):
    uppercase = ""
    digit = ""
    specialCharacter = ""
    if(len(password)>=8):
        for char in password:
            if(char.isupper()):
                uppercase+=char
            if(char.isnumeric()):
                digit+=char
            if(not char.isalnum()):
                specialCharacter+=char
    else:
        return False, 'Invalid Password, the length should be greater than 8'
    if(len(uppercase)>=1 and len(specialCharacter)>=1 and len(digit)>=1):
        return True, 'Valid password'
    else:
        return False, 'Invalid password'

print(password_validation('Ar$s@alaNnn123'))
print(password_validation('Ar$s@alaNnn'))
print(password_validation('Ar$'))
print(password_validation('AralaNnn123'))
print(password_validation('ralann12334'))