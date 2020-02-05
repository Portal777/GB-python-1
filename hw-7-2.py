# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbstractClass):
    title = "Одежда"
    value = None
    result = 0

    # не понятно как здесь сослаться на обьекты (экземпляры классов) и сложить их значения (впихнуть сюда строку №63)
    @property
    def consumption(self):
        return None


class Coat(Clothes):

    def __init__(self, v):
        self.title = "Пальто"
        self.value = v

    @property
    def consumption(self):
        self.result = round(self.value / 6.5 + 0.5, 2)
        return f'Расход ткани для "{self.title}" - {self.value} размера = {round(self.value / 6.5 + 0.5, 2)}'


class Costume(Clothes):

    def __init__(self, h):
        self.title = "Костюм"
        self.value = h

    @property
    def consumption(self):
        self.result = round(2*self.value + 0.3, 2)
        return f'Расход ткани для "{self.title}" - на рост {self.value} = {round(2*self.value + 0.3, 2)}'


my_1 = Clothes

my_2 = Coat(35)
print(my_2.consumption)

my_3 = Costume(183)
print(my_3.consumption)

print(f'Общий расход ткани = {my_2.result + my_3.result}')

# print(f'\n{Coat.title}, {Coat.value}')
