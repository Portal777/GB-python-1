
num = int(input('Введите целое положительное число, для нахождения большей цифры: '))

most = 0
calc = 0
while num > 0:

    calc = num % 10

    if calc > most:
        most = calc
        num = num // 10

    elif num % 10 == 9:
        print('Наибольшая цифра - 9')
        break

    else:
        num = num // 10

if most != 0 and num != 9:
    print('\nНаибольшая цифра = ', most)
elif most == 0:
    print('\n0 - не подходит под условия')

print('\nКонец')
