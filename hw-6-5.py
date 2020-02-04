# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = '"Канцелярская принадлежность"'

    def draw(self):
        return f'\nЗапуск отрисовки с помощью {self.title}'


class Pen(Stationery):

    def draw(self):
        self.title = '"Ручка"'                # долго приходил к данной строчке)
        return f'Вы взяли {self.title}'


class Pencil(Stationery):

    def draw(self):
        self.title = '"Карандаш"'
        return f'Вы взяли {self.title}'


class Handle(Stationery):

    def draw(self):
        self.title = '"Маркер"'
        return f'Вы взяли {self.title}'


first = Stationery()
print(first.draw())

pen = Pen()
print(pen.draw())

pencil = Pencil()
print(pencil.draw())

handle = Handle()
print(handle.draw())
