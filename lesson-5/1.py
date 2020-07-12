try:
    while True:
        with open('01.txt', 'w', encoding='utf-8') as file:
            a = input('введите что нибудь ')
            print(a, file=file)
            if a == '':
                break
except IOError:
    print('Ошибка ввода-вывода')
    file.close()