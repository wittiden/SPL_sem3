class Stationery:
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашем")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

obj = Stationery()
obj1 = Pen()
obj2 = Pencil()
obj3 = Handle()

obj.draw()
obj1.draw()
obj2.draw()
obj3.draw()