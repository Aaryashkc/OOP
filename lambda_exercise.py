my_list = [10,12,3,4,95,6,15]

print(list(map(lambda x: x*x, my_list)))

a= [(0,2), (4,3), (9, 9), (10,-1)]


my_list1 = [10, 2, 3, 4, 5, 6, 15]
soul = []

while my_list1:
    highest = my_list1[0]

    for number in my_list1:
        if number > highest:
            highest = number

    soul.append(highest)
    my_list1.remove(highest)

print(soul)