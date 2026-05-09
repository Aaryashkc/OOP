my_numbers = list(range(10))

print(list(map(lambda x: x*2, my_numbers)))

print(list(filter(lambda x: x%2 !=0, my_numbers)))