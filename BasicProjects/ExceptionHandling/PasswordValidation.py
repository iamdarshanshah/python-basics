"""
Prompt a user to enter a password
Check the length and make sure it is atleast 8 char. long
if length < 8 char
create a custom exception : InvalidPasswordException
raise the exception, handle it and display a user friendly message
"""


class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg


password = input("Enter a password :: ")
passLenght = len(password)

if passLenght > 8:
    print("Valid password")
else:
    try:
        raise InvalidPasswordException("Invalid password as length less than 8")
    except InvalidPasswordException:
        print("Try a password with atleast 8 characters.")
