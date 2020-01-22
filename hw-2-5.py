
main_list = [7, 5, 3, 3, 2]

while True:
    user_num = input('Введите числовое значение рейтинга, либо оставьте пустую строку для выхода: ')

    if user_num == '':
        break

    main_list.append(float(user_num))  # float - для проверки условия размещения после изначальных чисел
    print(f'Вы ввели число: {user_num}. Результат: {sorted(main_list, reverse=True)}')
