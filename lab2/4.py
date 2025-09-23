flag = True
while flag:
    try:
        x = int(input("Введите число: "))
        x += 5
        print(x)
        flag = False
    except ValueError:
        print("Введите число")
    # else:
    #     print("Другая ошибка")
    finally:
        print("Продолжаем")