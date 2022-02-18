"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа,
начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
"""
def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10): #генерирует 10 чисел начиная с указанного
        print(i)
gen1()

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
def gen2():
    list = [1, 107, None, "this_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10): #повторение элементов списка будет прекращено после 10ого повторения
        print(el)
gen2()