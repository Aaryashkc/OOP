class PlayerCharacter:
    def __init__(self, name, age, phone):
        self.name = name #attributes / properties
        self.age = age
        self.phone = phone

    def run(self):
        print('run')

player1 = PlayerCharacter("aaryash", 50, 9855067253)

print(player1.name, player1.age, player1.phone)