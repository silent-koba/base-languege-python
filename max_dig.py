print('Здравствуйте, сегодня мы будем искать самую большую цифру в введенном числе')
user_number = int(input('Введите число '))
max_dig = user_number%10
user_number = user_number//10
while user_number > 0:
	if user_number%10 > max_dig:
		max_dig = user_number%10
	user_number = user_number//10
print('Максимальная цифра в вашем числе, это ', max_dig)