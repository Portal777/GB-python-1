# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class MyError(Exception):

    def __init__(self, report):
        self.report = report


num1 = input("Введите делимое: ")
num2 = input("Введите делитель: ")

try:
    num1, num2 = int(num1), int(num2)
    if num2 == 0:
        raise MyError("\nНельзя делить на ноль!")
except ValueError:
    print("\n Вы ввели не число!")
except MyError as err:
    print(err)
else:
    print(f"Все хорошо. Частное: {num1 / num2}")
