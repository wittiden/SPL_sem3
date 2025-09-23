products = {
    "торт": ["мука, сахар, яйца", 5, 1000 ],
    "пирожное": ["бисквит, крем, шоколад", 3.5, 500],
    "маффин": ["мука, яйца, шоколад, орехи", 2.0, 300],
    "эклер": ["заварное тесто, крем", 4.0, 400],
    "печенье": ["мука, масло, сахар, ваниль", 1.5, 800]
}
totalPrice = 0
flag5 = True

while True:

    print("1 - Просмотр описания")
    print("2 - Просмотр цены")
    print("3 - Просмотр поличества")
    print("4 - Вся информация")
    print("5 - Покупка")
    print("6 - Выход")
    number = int(input("Введите номер действия: "))
    if number == 1:
        for key, value in products.items():
            print(key, ":", end = " ")
            print(value[0])
    elif number == 2:
        for key, value in products.items():
            print(key, end = " ")
            print(value[-2])
    elif number == 3:
        for key, value in products.items():
            print(key, end = " ")
            print(value[-1])
    elif number == 4:
        print(products)
    elif number == 5:
        prName = input("Введите название продукции (n, чтобы выйти): ")
        if prName == "n":
            break

        if prName in products:
            value = products[prName]
            prCount = int(input("Введите количество гр: "))
            if prCount < 1:
                break
            if prCount <= value[-1]:
                totalPrice += prCount / 100 * value[-2]
                value[-1] -= prCount
                print(totalPrice, "руб", end=" ")
                print(value[-1], "- осталось")
            else:
                print("Недостаточно товара!")
        else:
            print("Неверное значение")
    elif number == 6:
        break
