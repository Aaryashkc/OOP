class User():
    def __init__(self, email):
        self.email= email


    def is_signed_in(self):
        print('yes')


class Wizard(User):
    def __init__(self, attack, defense, aura, email):  #mention everything from super class/ parent for this to work
        super().__init__(email)
        self.attack= attack
        self.defense= defense
        self.aura= aura


wizard1= Wizard(1000, 1000, 50, 'aaryashkc@gmail.com')

# wizard1.is_signed_in()
print(wizard1.email)