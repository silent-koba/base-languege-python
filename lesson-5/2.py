num_rows = 0
with open('02.txt', encoding='utf-8') as file:
    for line in file:
        num_words = 0
        num_rows += 1
        words = line.split()
        num_words += len(words)
        print(f'В {num_rows} строке {num_words} слов')
