with open('04.txt') as reading:
    text = reading.read()

text = text.replace("one", "один"), \
       text.replace("two", "два"), \
       text.replace("three", "три"), \
       text.replace("four", "четыре")

with open("04-1.txt", "w") as writing:
    for i in range(0, 4):
        writing.write(text[i])
