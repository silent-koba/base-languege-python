sr_doh = 0
i = 0
with open('03.txt', encoding='utf-8') as f:
    for line in f:
        my_list = line.split()
        if int(my_list[1]) <= 20000:
            print(my_list[0])
            i += 1
        sr_doh = (sr_doh + int(my_list[1]) / i)
print('Средний доход составляет ', round(sr_doh, 2))
