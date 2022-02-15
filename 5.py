my_list = [8, 6, 4, 3, 2]

n = int(input('количество ввода: '))
for it in range(n):
    number = int(input('введите рейтинг: '))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, float(number))
    print(my_list)