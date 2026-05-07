class PlayerCharacter:
    def __init__(self, name, age, phone):
        self.name = name  # attributes / properties
        self.age = age
        self.phone = phone

    def run(self):
        print('run')
        return "done"


player1 = PlayerCharacter("aaryash", 50, 9855067253)

print(player1.name, player1.age, player1.phone)
print(player1.run())


class Cat:

    def __init__(self, name='none', age=0):
        self.name = name
        self.age = age

    @classmethod
    def adding_age(cls, age1, age2):
        return age1 + age2

    @staticmethod
    def adding_age2(age1, age2):
        print (age1 + age2)


cat1 = Cat('denail', 20)
cat2 = Cat('den', 18)
cat3 = Cat('dena', 90)

cat= Cat()
cat.adding_age2(cat1.age, 10)


def oldest_cat(*args):
    return max(args)


print(f'the oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
print(f'The sum of cat1 and cat 2 is {Cat.adding_age(cat1.age, cat2.age)}')

