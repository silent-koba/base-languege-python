print('Это программа конвертации времени')
user_time = int(input('Введите время в секундах: '))
hh = user_time//3600
mm = (user_time - hh * 3600)//60
ss = (user_time - hh * 3600) - mm * 60
if hh < 10:
    hh = '0' + str(hh)
else: hh = str(hh)
if mm < 10:
    mm = '0' + str(mm)
else: mm = str(mm)
if ss < 10:
    ss = '0' + str(ss)
else: ss = str(ss)
time = hh + ':' + mm + ':' + ss
print('В стандартном формате это', time)