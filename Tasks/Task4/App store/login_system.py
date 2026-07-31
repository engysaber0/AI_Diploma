import random
class LoginSystem:
    """
    handles the login flow for a user, checking the username, the password, and a random verification code
    attributes:
    saved_username (str): the username that is stored
    saved_password (str): the password that is stored
    code (int): the verification code that gets generated
    """
    def __init__(self, saved_username, saved_password):
        self.saved_username = saved_username
        self.saved_password = saved_password
        self.code = None

    def check_username(self, typed_username):
        """
        checks if the typed username matches the saved one
        args:
        typed_username (str): the username the user typed in
        returns:
        bool: true if it matches, false if not
        """
        return typed_username == self.saved_username

    def check_password(self, typed_password):
        """
        checks if the typed password matches the saved one
        args:
        typed_password (str): the password the user typed in
        returns:
         bool: true if it matches, false if not
        """
        return typed_password == self.saved_password

    def make_code(self):
        """
        makes a random four digit code and saves it for later
        returns:
        int: the code that got made
        """
        self.code = random.randint(1000, 9999)
        return self.code

    def check_code(self, typed_code):
        """
        checks if the typed code matches the one that was made
        args:
        typed_code (int): the code the user typed in
        returns:
        bool: true if it matches, false if not
        """
        return typed_code == self.code

    def login(self):
        """
        runs the whole login flow, from typing the username all the way to getting let in after the right code is typed
        returns:
        bool: true once the login is done
        """
        username = input("Enter username: ")
        while not self.check_username(username):
            username = input("This username is incorrect. Enter username again: ")

        password = input("Enter password: ")
        while not self.check_password(password):
            password = input("This password is incorrect. Enter password again: ")

        new_code = self.make_code()
        print("Your verification code is:", new_code)

        typed_code = int(input("Enter verification code: "))
        while not self.check_code(typed_code):
            typed_code = int(input("This verification code is incorrect. Enter verification code again: "))

        print("Welcome")
        return True