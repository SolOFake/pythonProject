class Foo:

    def __init__(self, *args):
        self.args = args

    def sum(self, *indices):
        result = 0
        for index in indices:
            result += self.args[index]

        return result


foo = Foo(10, 20, 30, 100)
print(foo.sum(0, 1, 3))  # 130

# класс который будет принимать неопределенное количество аргументов.
# а потом к ним можно будет обратиться по индексу [ ] и засумировать значения
# выбранных индексов ;D
# self.result = sum(args)
