time = int(input('Введите время в секундах (числами): '))

seconds = time % 60
minutes = (time - seconds) / 60 % 60
hours = (time - seconds) // 60 // 60

# while minutes >= 60:
#     minutes -= 60
#     hours += 1

print(f"чч:{hours}, мм:{int(minutes)}, сс:{seconds}")
