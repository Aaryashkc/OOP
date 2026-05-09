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