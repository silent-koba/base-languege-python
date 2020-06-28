vir = int(input('Введите сумму выручки '))
izd = int(input('Введите сумму издержек '))
if vir > izd:
	print('Фирма работает на прибыль')
	rent = (vir - izd)/vir
	sotrudniki = int(input('Укажите количество сотрудников в фирме '))
	prib_sotr = (vir - izd) / sotrudniki
	print('Фирма получила', prib_sotr, 'прибыли на каждого сотрудника')
elif izd > vir:
	print('Фирма работает в убыток')
else: print('Фирма работает в 0')