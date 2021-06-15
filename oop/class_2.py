
import classOne
p = classOne.Person2()
print(p)



class Character:
    def __init__(self, actual_race):  # конструктор
        self.character_race = actual_race

    def akb(self, abra, ada, bra=3):

        self.super_abra = abra
        self.super_ada = ada
        self.super_bra = bra
        return self.super_ada + self.super_ada + self.super_bra


unit = Character(100)
print(unit.akb(1, 2))
print(type(unit))

print(unit.character_race, type(unit.character_race))
