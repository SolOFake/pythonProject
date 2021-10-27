class Table:
    def __init__(self, le, w, h):
        self.length = le
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, le, w, h, p):
        super().__init__(le, w, h)
        self.places = p


t2 = KitchenTable(1, 2, 3, 4)