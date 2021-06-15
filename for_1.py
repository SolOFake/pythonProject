#
# #                    работа с цыклом for
# for i in range(1, 9, 2):
#     print(i)
# else:
#     print('Цикл for закончен\n')
#
# a = range(1, 5)
# print(a)
#
# b = list(range(1, 5))
# print(b)
#
#
# #                    работа оператора break
# while True:
#     s = input('Введите что-нибудь: ')
#     if s == 'выход':
#         break
#     print('Длина строки:', len(s))
# print('Завершение')


#                    работа с оператором continue
while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) <= 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')
    # Разные другие действия здесь...
print('произошел выход из цикла')

def sayHello():
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции

sayHello()  # ещё один вызов функции
