my_list = [2, 3, 3, 5, 7]
user_rate = int(input('Введите ваш рейтинг: '))
for el in my_list:
    if user_rate in my_list:
        index = my_list.index(user_rate)
        my_list = my_list.insert(index, user_rate)
# i = 1
# for el in my_list:
#     if my_list[0] >= user_rate:
#         my_list.insert(0, user_rate)
#     elif my_list[-1] < user_rate:
#         my_list.insert(-1, user_rate)
#     elif my_list[i] == user_rate:
#         my_list.insert(i, user_rate)
#     elif my_list[i] < user_rate and user_rate < my_list[i+1]:
#         my_list.insert(i+1, user_rate)
my_list = my_list.reverse()
print(my_list)