class Building:
    def __init__(self, year = None, city = None):
        self.__year = year
        self.__city = city

    def set_data(self, year, city):
        self.__year = year
        self.__city = city
    def get_data(self):
        return print(self.__year, self.__city)

    @staticmethod
    def bStandarts():
        print("определяют требования к размещению зданий на участке, их высоте, а также к внутренним параметрам помещений, включая минимальные размеры комнат, ширину проходов и технические параметры систем жизнеобеспечения")


class School(Building):
    def __init__(self, year = None, city = None):
        super().__init__(year, city)

    @staticmethod
    def bStandarts():
        print("Стандарты застройки школ включают требования к территории (площадь, озеленение), этажности зданий (обычно не более 3 этажей), размерам и расположению помещений (классы, рекреации, санитарные узлы), а также к обеспечению безопасности и санитарных норм")

class Mall(Building):
    def __init__(self, year = None, city = None):
        super().__init__(year, city)


building = Building()
school = School()
mall = Mall()

building.set_data(2020, "minsk")
building.get_data()
building.bStandarts()
print("\n")
school.bStandarts()