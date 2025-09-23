minSize = int(input("Введите диапазон (от x до y):\n"))
maxSize = int(input())
primeNumber = 0

if maxSize > minSize:
    for i in range(minSize, maxSize+1):
        if i <= 1:
            continue
        count = 0

        for j in range(1, i+1):
            if i % j == 0:
                count += 1

        if count == 2:
            primeNumber += 1
    print(primeNumber)
else:
    print("error")