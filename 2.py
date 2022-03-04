"""

2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""



from abc import ABC, abstractmethod


class Clothes(ABC):
    instances = []

    def __init__(self, param):
        self.param = param
        Clothes.instances.append(self)

    @abstractmethod
    def cloth_consumption(self):
        pass

    def __del__(self):
        if self in Clothes.instances:
            Clothes.instances.remove(self)


class Coat(Clothes):
    @property
    def cloth_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def cloth_consumption(self):
        return round((self.param * 2 + 0.3) / 100, 2)


coat1 = Coat(50)
costume1 = Costume(160)
costume2 = Costume(210)

total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f"Общий расход ткани: {total_cloth_consumption}")
coat1.__del__()

total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f"Общий расход ткани: {total_cloth_consumption}")
