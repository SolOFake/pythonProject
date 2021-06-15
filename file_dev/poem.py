
poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
f = open('poem.txt', 'w')  # открываем для записи (writing)
f.write(poem)  # записываем текст в файл
f.close()  # закрываем файл
with open("poem.txt", "a") as f:  # открываю на запись в конец
    for line in range(3):  # спрашиваю инпут 3 раза
        print(input("Вееди че то: "), file=f)  # пишу в файл file=f

with open("poem.txt", "r") as f:
    text = f.readlines()  # считываю строки
    print(text[5])  # вывожу 5 строку

# если не указан режим, по умолчанию подразумевается
# режим чтения ('r'eading)
# for i, x in enumerate(lines):
#     if i == 2:
#     print(x)
# закрываем файл
