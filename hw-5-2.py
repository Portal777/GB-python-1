# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open("5-2-count.txt", 'r', encoding='UTF-8')

lines = 0
words = 0
symbols = 0

for lin in file:
    lines += 1
    its_split = lin.split(' ')
    words += len(its_split)
    for sym in lin:
        if sym != ' ' and sym != '\n':  # отбрасываем пробелы и переход на новую строку
            symbols += 1

file.close()

print(f'\nКоличество строк: {lines}')
print(f'\nКоличество слов: {words}')
print(f'\nКоличество символов: {symbols}')
