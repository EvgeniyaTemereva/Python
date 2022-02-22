"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open('new_file.txt', 'a') as file:
    while True:
        user_answ = input('Write smth: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break