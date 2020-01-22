
user_string = input('Введите несколько слов, разделенных пробелами')

user_string = user_string.split()

for id, item in enumerate(user_string):
    if len(item) > 10:
        print('Строка №', id+1, item[:9])
    else:
        print('Строка №', id+1, item)
