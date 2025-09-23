def workWithParametres(parametr):
    if type(parametr) == str:
        count = 0
        for i in parametr:
            if i.isalpha():
                count+=1
        print(count)

    elif type(parametr) == int:
        count = 0
        for i in str(parametr):
            if int(i) % 2 != 0:
                count+=1
        print(count)

    elif type(parametr) == list:
        words = 0
        digits = 0
        for i in parametr:
            if str(i).isdigit():
                digits+=1
            if str(i).isalpha():
                words+=1
        print(digits, words)

    elif type(parametr) == tuple:
        print(len(parametr))

workWithParametres([1,1,2,3,3, "g", "f"])