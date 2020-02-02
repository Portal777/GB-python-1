# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    name = ''
    surname = ''
    position = ''
    __income = {"wage": 0, "bonus": 0}

    def __init__(self):
        self.name = input('Введите имя')
        self.surname = input('Введите фамилию')
        self.position = input('Ведите должность')
        self.__income.update({"wage": 123})
        print(self.__income)


class Position(Worker):

    def get_full_name(self):
        pass

    def get_total_income(self):
        pass


first = Position()
first.get_full_name()
