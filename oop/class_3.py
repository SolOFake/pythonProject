class Boom:
    def __init__(self, *args, act=0):  # конструктор
        self.actual_act = act
        self._args = self.parse_arguments(args)

    # походу нужно както цыклом перебрать и возвращаять аргументы
    # Для того что бы например взять и обратиться с определенному аргументу self._args[2]
    #отом перебирай их в цикле и по ключу обзывай переменными.
    # Ну а вообще неопределенное количество аргументов это зло.
    # Ты скажи что ты хочешь передавать в качестве аргументов и
    # что потом с этим делать, может твоя задача решается гораздо проще
    @staticmethod
    def parse_arguments(_args): # тут явно 3 возвращаю но даже это не работает ;D
        return _args[0], _args[1], _args[2]

    def indexing(self):
        pass

    def summa(self):
        return self.actual_act + self.parse_arguments(_args)


pt = Boom(2, 3, 100, act=1)
print(pt.summa())









# можно сделать неопределённое количество аргументов
# def a(*args):
#    return sum(args)
# assert(a(1, 2, 3), 6)
# unit = Character(100)
# print(unit.akb(1, 2, 3))
#
