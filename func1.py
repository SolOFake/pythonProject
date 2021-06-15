
# def say_hello():
#     print('Привет, Мир!')  # блок, принадлежащий функции
# # Конец функции
#
#
# say_hello()  # ещё один вызов функции
#
#
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
#
#
# print_max(3, 4)  # прямая передача значений
# x = 5
# y = 7
# print_max(x, y)


# def my_sum(a, b):
#     print('Сумма 2 чисел равна:', a + b)
#
#
# my_sum(5, 15)


# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(5, 15))

# x = 50
# print('x за пределами функции 50', x)
#
#
# def func(x):
#     print('x равен 50', x)
#     x = 2
#     print('Замена локального x на 2', x)
#
#
# func(x)
# print('x по-прежнему 50', x)


#                   слово global


# x = 50
#
#
# def func11():
#     global x
#
#     print('x равно', x)
#     x = 2
#     print('Заменяем глобальное значение x на', x)
#
#
# func11()
# print('Значение x составляет', x)


#                  слово nonlocal

# x = 0
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print('inner:', x)
#
#     inner()
#     print('outher:', x)
#
# outer()
# print('global:', x)

# def say(message, times = 1):
#     print(message * times)
# say('Привет')
# say('Мир', 5)
#
#
#
# def func(a, b=5, c=10):
#     print('a равно', a, ', b равно', b, ', а c равно', c)
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)


#                переменное число параметров *args и **kwargs

# def total(a=5, *numbers, **phonebook):
#     print('a', a)
#     #  проход по всем элементам кортежа
#     for single_item in numbers:
#         print('single_item', single_item)
#     #  проход по всем элементам словаря
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
#
# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
#
# total(10, 1, 2, 3)
# # total(10, 1, 2, 3, extra_number=50)

# def maximum(x, y):
#     if x > y:
#         return '1 больше', x
#     elif x == y:
#         return 'Числа равны.'
#     else:
#         return '2 больше', y
#
#
# print(list(maximum(5, 3)))



# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'Числа равны.'
#     else:
#         return y


def printMax(x, y):
    '''Выводит максимальное из двух чисел.

Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)
