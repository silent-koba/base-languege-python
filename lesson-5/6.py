file = open('06.txt', encoding='utf-8')
for line in file:
    total, current = 0, ''
    for ch in line:
        if ch.isdigit():
            current += ch
        elif current != '':
            total += int(current)
            current = ''
    if current != '':
        total += int(current)
    print(total)
file.close()