"""
A user and admin class that can be used as a module
"""

class User:
    """A simple user info and greeting."""

    def __init__(self, first_name, last_name, age, hobby):
        """Intialize attributes to use later."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        """Later happend!:D Description of oneself"""
        print('\n' + self.first_name.title() + " " +
              self.last_name.title() + " is " + str(self.age) +
              " and their hobby is " + self.hobby + '.')

    def greet_user(self):
        """Greeting from the great systematic response"""
        print("Welcome " + self.first_name.title() + " " +
              self.last_name.title() +
              "! We hope you like your experience with us.")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        self.login_attempts += 1
        print(self.login_attempts)  # Just to check if method works

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0"""
        self.login_attempts = 0
        print(self.login_attempts)  # Just to check if method works


class Privileges():
    """Simple attempt to show privileges"""

    def __init__(self, user_type="Admin"):
        self.user_type = user_type
        self.privileges = ["can add post", "can delete post", "can ban user",
                           "Can add User"]

    def show_privileges(self):
        print(self.user_type + " privileges are:")
        for privilege in self.privileges:
            print(" -" + privilege)


class Admin(User):
    """Simple attempt to represent an Admin user"""

    def __init__(self, first_name, last_name, age, hobby):
        super(Admin, self).__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()