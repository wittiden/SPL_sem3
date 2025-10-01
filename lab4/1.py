import math as mth
class Calculator:
    def __init__(self, first = 0.0, second = 0.0):
        self.__first = first
        self.__second = second
    def set_data(self, first, second):
        self.__first = first
        self.__second = second

    def get_data(self):
        print("\nЧисло 1: ", self.__first, "\nЧисло 2: ",  self.__second)

    def additionEl(self):
        result = self.__first + self.__second
        print("Результат: ", result)
    def negationEl(self):
        result = self.__first - self.__second
        print("Результат: ", result)
    def multiplyEl(self):
        result = self.__first * self.__second
        print("Результат: ", result)
    def sqrtEl(self):
        res1 = mth.sqrt(self.__first)
        res2 = mth.sqrt(self.__second)
        print("Результат 1: ", res1, "\nРезультат 2: ", res1)
    def powEl(self):
        result = self.__first ** self.__second
        print("Результат: ", result)


x = float(input("Введите 1 число: "))
y = float(input("Введите 2 число: "))
clc = Calculator(x, y)

flag = True

while(flag):
    print("Выберите действие (0 для выхода): ")
    print ("1 + 2")
    print ("1 - 2")
    print ("1 * 2")
    print ("√1, √2")
    print ("1^2")
    choose = input("Введите номер действия: ")

    if choose == "1":
        clc.additionEl()
    if choose == "2":
        clc.negationEl()
    if choose == "3":
        clc.multiplyEl()
    if choose == "4":
        clc.sqrtEl()
    if choose == "5":
        clc.powEl()
    if choose == "0":
        flag = False

