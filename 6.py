"""
 * Реализовать структуру данных «Товары».
 Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
 В кортеже должно быть два элемента — номер товара и словарь с параметрами,
 то есть характеристиками товара: название, цена, количество, единица измерения.
 Структуру нужно сформировать программно, запросив все данные у пользователя.

"""


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        f_copy[f] = int(pro) if f in 'цена количество' and pro.isdigit() else pro  # Меняем тип числовых свойства
        analytics[f].append(f_copy[f])  # Добавляем свойство в аналитику
    goods.append((num, f_copy))  # Добавляем свойство в список товаров
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)