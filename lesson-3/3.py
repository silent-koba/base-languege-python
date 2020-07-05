def my_func(x, y, z):
    max_sum = 0
    if y > x < z:
        max_sum = z + y
    elif x > y < z:
        max_sum = z + x
    else: max_sum = x + y
    return max_sum

x = int(input('Введите первое число: '))
z = int(input('Введите второе число: '))
y = int(input('Введите третье число: '))
print(my_func(x, y, z))