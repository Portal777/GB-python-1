# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтеры, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def send_to_warehouse(self):
        pass

        # , department, types, model, quantity, *unique):
        # t.update({2: {21: 22}, 3: {31: 33}})
        # w = {"1": {"11": 11}, "2": {"22": 22}}
        # print(w["1"]["11"])
        # Warehouse.store.get(department).get(types).update({model: {f'{quantity} шт.', unique}})


class Warehouse(MyAbstractClass):
    store = {"Офис": {"Принтеры": {}, "Сканеры": {}, "Ксероксы": {}},
             "Цех": {"Принтеры": {}, "Сканеры": {}, "Ксероксы": {}},
             "Склад": {"Принтеры": {}, "Сканеры": {}, "Ксероксы": {}}}

    def send_to_warehouse(self):
        return None

    @staticmethod
    def watch_department(name):
        return f'\n"{name}" располагает следующей техникой:{Warehouse.store.get(name)}\n'


class Equipment(Warehouse):

    def __init__(self, department, types, model, quantity):
        self.department = department
        self.types = types
        self.model = model
        self.quantity = quantity

    def send_to_warehouse(self):
        return None


class Printer(Equipment):

    def __init__(self, department, model, quantity, types="Принтеры", color=False):
        super().__init__(department, types, model, quantity)
        self.color = color

    def send_to_warehouse(self):
        # t.update({2: {21: 22}, 3: {31: 33}})
        # w = {"1": {"11": 11}, "2": {"22": 22}}
        # print(w["1"]["11"])
        Warehouse.store.get(self.department).get(self.types).update({self.model: {f'{self.quantity} шт.', self.color}})


class Scanner(Equipment):

    def __init__(self, department, types, model, quantity, custom_size=False):
        super().__init__(department, types, model, quantity)
        self.size = custom_size


class Xerox(Equipment):

    def __init__(self, department, types, model, quantity, double_sided=False):
        super().__init__(department, types, model, quantity)
        self.double = double_sided


# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


def run_menu():
    variants = ["1", "2", "3", "4"]

    while True:
        answ = input("Выберите вариант: 1 - Добавить технику в отделы; 2 - Посмотреть список техники в отделах; "
                     "3 - Закрыть программу: ")

        if answ == "1":

            while True:

                add_answ = input("Выберите отдел, в который хотите добавить технику: "
                                 "1 - 'Офис'; 2 - 'Цех'; 3 - 'Склад'; 4 - Выйти из данного меню : ")

                if add_answ in variants:

                    if add_answ == "4":
                        break

                    while True:

                        type_answ = input("Выберите тип техники: 1 - 'Принтеры', 2 - 'Сканер', 3 - 'Ксерокс'; "
                                          "4 - Выйти из данного меню : ")

                        if type_answ in variants:
                            # дописать добавление техники на выбранный склад, с возможностью внесения
                            # типа-модели-количества и доп.свойства для каждого типа техники

                            if type_answ == "4":
                                break

                            while True:

                                menu_answer = input("1 - 'Продолжить добавление', 2 - Посмотреть склад; "
                                                    "3 - 'Посмотреть отдел', 4 - Выйти из данного меню : ")

                                if menu_answer in variants:

                                    if menu_answer == "4":
                                        break

                                else:
                                    print("\nВы ввели некорректный ответ\n")
                                    continue

                        else:
                            print("\nВы ввели некорректный ответ\n")
                            continue

                else:
                    print("\nВы ввели некорректный ответ\n")
                    continue
        elif answ == "2":
            print(f'\n{Warehouse.store}\n')

        elif answ == "3":
            print('\nПрограмма завершена')
            exit()
        else:
            print("\nВы ввели некорректный ответ\n")


# my_store = Warehouse()
# print(my_store.store)
# print(watch_department("Офис"))

print(Warehouse.watch_department("Офис"))
# Warehouse.send_to_warehouse("Офис", "Принтеры", "af23", 2)

firts = Printer("Офис", "HP", 5)
firts.send_to_warehouse()
second = Printer("Офис", "Xerox", 1)
second.send_to_warehouse()
third = Printer("Офис", "Xerox", 3)
third.send_to_warehouse()

print(Warehouse.watch_department("Офис"))

#run_menu()



# for i in store:
#     store.update({i: {"Принтеры": None, "Сканер": None, "Ксерокс": None}})
# print(store)
# for i in store:
#     print(i, store.get(i))


