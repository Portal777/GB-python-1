
user_list = []

while True:
    add_elements = input('Введите элемент, для добавлениея список. Чтобы прекратиить добавление элементов в список,'
                         'оставьте поле пустым: ')
    if add_elements == '':
        break
    else:
        user_list.append(add_elements)

print('Изначальный список: ', user_list)

for id, item in enumerate(user_list):
    if id + 1 == len(user_list) and len(user_list) % 2 != 0:
        break
    elif id % 2 == 0:
        first_value = user_list[id]
        second_value = user_list[id+1]
        user_list[id] = second_value
        user_list[id+1] = first_value

print('Измененный список: ', user_list)

# Времени ушло примерно час, может больше
