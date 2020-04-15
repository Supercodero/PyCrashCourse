class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print("User's name is "+self.first_name.title()+" "+self.last_name.title())

    def greet_user(self):
        print("Hello, "+self.first_name.title()+" "+self.last_name.title())
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()
    


user = User("Helen","Keller")
user.describe_user()
user.greet_user()
for n in range(14):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

admin = Admin("Mm","miya")
admin.describe_user()
admin.privileges.show_privileges()