monthes = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
spring = 'Весна'
autumn = 'Осень'
summer = 'Лето'
winter = 'Зима'
user_month = int(input('Введите номер месяца: '))
index = monthes.index(user_month)
if index >= 0 and index < 3:
    print(spring)
elif index >= 3 and index < 6:
    print(summer)
elif index >= 6 and index < 9:
    print(autumn)
else: print(winter)
