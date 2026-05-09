class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def call_name(self):
        return self.name

    def call_age(self):
        print(f'{self.name} is {self.age} years old')

Person1=Person('Aaryash', 20)

print(Person1.call_name())
Person1.call_age()


class Gun:
    def __init__(self, damage, ammo):
        self.damage= damage
        self.ammo= ammo

    def deal_damage(self):
        print(f'Player deal {self.damage} damage')

    def deal_ammo(self):
        print(f'Player has {self.ammo} ammo')

Round1=Gun(1000, 100)
Round1.deal_damage()
Round1.deal_ammo()