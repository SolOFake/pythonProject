class Person:
    def __init__(self, a1, b1):
        self.aa1, self.bb1 = a1, b1

    def prt(self):
        return sum([self.aa1, self.bb1])


class Person2(Person):
    def __init__(self, a2, b2):
        super().__init__(a2, b2)  # прокси
        self.aa2, self.bb2 = a2, b2


pt = Person(10, 20)
# print(pt.prt())
print(pt.aa1)

pt2 = Person2(11, 22)
# print(pt2.prt())
print(pt2.aa1)
print(pt2.aa2)
