# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes:
    title = "Одежда"
    value = None

    def total_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, V):
        self.title = "Пальто"
        self.value = V

    @property
    def consumption(self):
        return f'Расход ткани для "{self.title}" - {self.value} размера = {self.value / 6.5 + 0.5}'


class Costume(Clothes):

    def __init__(self, H):
        self.title = "Костюм"
        self.value = H

    @property
    def consumption(self):
        return f'Расход ткани для "{self.title}" - на рост {self.value} = {2*self.value + 0.3}'


my_1 = Coat(35)
print(my_1.consumption)
my_2 = Costume(180)
print(my_2.consumption)

print(f'\n{Coat.title}, {Coat.value}')
