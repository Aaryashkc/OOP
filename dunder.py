class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def name_1(self):
        return f'{self.name} {self.price}'

    def __str__(self):
        return f'{self.price}'

    def __len__(self):
        return 10

# print(dir(Toy))
toy1= Toy('Toy', 200)

print(toy1)
print(len(toy1))
print(toy1.__str__())
print(str(toy1))
print(str(10))