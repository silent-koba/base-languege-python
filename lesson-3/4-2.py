def module(a):
    if a < 0:
        a = a * -1
    return a

def my_func(x,y):
    i = module(y)
    new_x = x
    if y < 0:
        if y == 0:
            new_x = 1
        else:
            while i > 1:
                new_x = new_x * x
                i -= 1
        new_x = 1/new_x
    else:
        if y == 0:
            new_x = 1
        else:
            while i > 1:
                new_x = new_x * x
                i -= 1
    return new_x

a=int(input())
b=int(input())
print(my_func(a,b))