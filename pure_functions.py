from functools import reduce

my_list = list(range(10))
your_list = list(range(10, 20))


# print(my_list)
# print(your_list)

def MultipleByTwo(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


multiple_by_two = list(map(MultipleByTwo, range(10)))

filter_odd = list(filter(check_odd, range(10)))

zip_list = list(zip(my_list, your_list))

print(multiple_by_two)
print(filter_odd)
print(zip_list)


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
