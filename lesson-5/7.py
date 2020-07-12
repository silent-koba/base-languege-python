import json
my_dict = {}
average = {}
my_list = []
my_newlist = []
result = 0
av_res = 0
i = 0
with open('07.txt', encoding='utf-8') as f:
    for line in f:
        lines = line.split()
        if int(lines[2]) > int(lines[3]):
            result = int(lines[2]) - int(lines[3])
            my_dict[lines[0]] = result
            i += 1
            av_res = av_res + result
average['Средняя выручка'] = av_res / i
my_newlist = my_list.append(my_dict)
my_newlist = my_list.append(average)
with open('07-1.json', 'w') as j:
    json.dump(my_newlist, j)
