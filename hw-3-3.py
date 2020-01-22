# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(n_1, n_2, n_3):
    func_list = [n_1, n_2, n_3]
    func_list.remove(min(func_list))
    print(func_list)
    the_sum = 0  # скопированная идея цикла, хорошая, если неизвестно сколько значений в списке/функции
    for xx in func_list:
        the_sum = the_sum + xx
    return the_sum


data = {'n_1': 0, 'n_2': 0, 'n_3': 0}
copy_data = data.copy()

i = 1
for n, item in enumerate(data):
    while True:
        try:
            enter = int(input(f'Введите число №{i}: '))
            copy_data.update({f'{item}': enter})
            i += 1
            break
        except ValueError:
            print(f'\nРазрешено вводить только числа.\n')

print(my_func(copy_data.get('n_1'), copy_data.get('n_2'), copy_data.get('n_3')))
