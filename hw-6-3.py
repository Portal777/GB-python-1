# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    # name = ''
    # surname = ''
    # position = ''
    # __income = {"wage": 0, "bonus": 0}

    def __init__(self):
        try:
            self.name = input('Введите имя: ')
            self.surname = input('Введите фамилию: ')
            self.position = input('Ведите должность: ')
            self.__income = {"wage": 0, "bonus": 0}
            self.wage = int(input('Введите оклад (числом): '))
            self.bonus = int(input('Введите размер премии (числом): '))
            self.__income.update({"wage": self.wage, "bonus": self.bonus})
        except ValueError:
            print('\nРазрешен ввод только числами!')


class Position(Worker):

    def get_full_name(self):
        return f'\nСотрудник: {self.name} {self.surname}, {self.position}.'

    def get_total_income(self):
        return f'Доход сотрудника, с учетом премии = ' \
               f'{self._Worker__income.get("wage")+self._Worker__income.get("bonus")}.'


second = Position()
print(second.get_full_name())
print(second.get_total_income())
