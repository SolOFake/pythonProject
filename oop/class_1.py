
# class Person:
#     def sayHi(self):
#         print('Привет! Как дела?')
#
#
# p = Person()
# p.sayHi()

class Point:

    x = 1
    y = 2

    def say(self):
        print(self)


pt = Point()  # Создаём объект класса.
pt.say()
print(dir(Point))
print(Point.__name__)

print(pt.x, pt.y)
print(id(pt), id(Point), sep="\n")
print('Опача:', id(pt.x), id(Point.x))
# print()
pt.x = 100
pt.t = 15
print('Опача:', id(pt.x), id(Point.x))
print(pt.x, pt.y)
print(id(pt), id(Point), sep="\n")
print(pt.__dict__)

pt2 = Point()
pt2.x = 5
pt2.y = 100
print(getattr(pt2, "x"))  # проверяем что содержит атрибут
print(getattr(pt2, "t", False))  # атрибут не существует, будет ошибка, но
#                                  можно указать возвращаемое значение Пр. 'False'
print(hasattr(pt2, "y"))  # првоерка на существование
print()

print(hasattr(pt2, 'z'))  # False
setattr(pt2, "z", 7)  # добавление нового атрибута
print(hasattr(pt2, 'z'))  # True
print(pt2.__dict__)  # вывод всех атрибутов
delattr(pt2, 'z')  # удаление атрибута
print(pt2.__dict__)

print(isinstance(pt2, Point))


class Point3D:
    x = 10
    y = 20
    z = 30


p = Point3D()
p1 = Point3D()
p2 = Point3D()

setattr(Point3D, "x", 11)
print(p.x)
print(dir(p))
delattr(Point3D, "z")
print(dir(p))
