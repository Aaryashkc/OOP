my_list= [params for params in "hello"]

soul= [char*2   for char in my_list]

complex_exer= [char**2 for char in range(0, 100) if char %2 != 0]


super_dict= {
    'a':123,
    'b':456,
    'c':789,
}

my_set= {char+1 for char in range(0, 100)}

print(my_set )

my_dict = {key:value**2 for key,value in super_dict.items()}
# my_dict1 = {key:value**2 for key,value in super_dict()}

print(my_dict)
# print(my_dict1)
print(complex_exer)

print(soul)
print(my_list)


my_dict2= {num:num*2 for num in range(0, 10)}
print(my_dict2)