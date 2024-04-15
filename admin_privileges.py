"""
An Admin class that can be used as a module
"""
from user import User

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