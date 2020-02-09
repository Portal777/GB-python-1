# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import calendar


class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, value):
        date_list = [int(i) for i in value.split("-")]
        return date_list

    @staticmethod
    def validation(value):
        if value[0] in range(1, 31) and value[1] in range(1, 13) and value[2] > 999:
            # в модуле calendar - реальный календарь, проверяем чтобы введенный пользователем день был в этом месяце
            if value[0] <= calendar.monthrange(value[2], value[1])[1]:
                return f"Дата: {value} - реально существует!"
            return "Такая дата реально не существует"
        else:
            return "Ввведите правильно дату (в формате: '01-01-2000')"
        # a = calendar.monthrange(2020, 2)
        # a[1]
        # 29 - последнее число месяца


print(Data.date_to_int("29-02-2011"))
print(Data.validation(Data.date_to_int("29-02-2011")))
print()

date1 = Data
date1_int = date1.date_to_int("20-09-999")
print(date1_int)
print(date1.validation(date1_int))
print()

date2 = Data
print(date2.date_to_int("30-1-2029"))
print(date2.validation(date2.date_to_int("30-1-2029")))
