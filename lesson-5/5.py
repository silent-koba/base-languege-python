summ = 0
with open('05.txt', 'w+') as f:
    a = input('Введите числа через пробел: ')
    print(a, file=f)
    for line in f:
        el = int(line.split())
        summ = summ + el
print(summ)
