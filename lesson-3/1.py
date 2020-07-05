def delenie(a, b):
    result = a / b
    return result
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
if b == 0:
    print('На 0 делить нельзя')
else:
    result = delenie(a,b)
    print(result)
