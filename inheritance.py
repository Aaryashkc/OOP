class User():
    def signed_in(self):
        print("signed in")

class Admin(User):
    pass

class Cat(Admin):
    pass
admin1= Admin()
cat1= Cat()

admin1.signed_in()
cat1.signed_in()
