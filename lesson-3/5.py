def global_summ(user_input):
    user_str_list = user_input.split()
    user_dig_list = list(map(float, filter(lambda i: i.isdigit(), user_str_list)))
    return sum(user_dig_list)
total = 0
while True:
    user_input = input('Введите числа через пробел, или букву "q" для выхода: ')
    total += global_summ(user_input)
    print(f'Сумма всех введенных чисел равна {total}')
    if 'Q' in user_input.upper():
        break
