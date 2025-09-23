def showArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

showArr(arr)
print('\n')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == j:
            arr[i][j] = 1
        elif i < j:
            arr[i][j] = 0
        elif i > j:
            arr[i][j] = 2

showArr(arr)