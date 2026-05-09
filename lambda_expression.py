from functools import reduce

my_numbers = list(range(10))

print(list(map(lambda x: x*2, my_numbers)))

print(list(filter(lambda x: x%2 !=0, my_numbers)))

print(reduce(lambda acc, item: acc + item, my_numbers))