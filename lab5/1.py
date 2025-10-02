import numpy as np

arr1 = np.zeros(10)
print("1:\n", arr1)

arr2 = np.full(10, 2.5)
print("2:\n", arr2)

arr3 = np.zeros(10)
arr3[4] = 1
print("3:\n", arr3)

arr4 = np.arange(10, 50)
print("4:\n", arr4)

arr5 = np.array([1,2,0,0,4,0])
indexes = np.nonzero(arr5)[0]
print("5:\n", indexes)

arr6 = np.eye(3)
print("6:\n", arr6)

arr7 = np.random.randint(1, 11, (10,10))
print("7:\n", arr7)
print("max:", arr7.max())
print("min:", arr7.min())

arr8 = np.random.randint(1, 11, 30)
print("8:\n", arr8)
print("average:", arr8.mean())

arr9 = np.zeros((8,8))
arr9[1::2, ::2] = 1
arr9[::2, 1::2] = 1
print("9:\n", arr9)

matrix1 = np.random.randint(1, 11, (5, 3))
print("matrix1:\n", matrix1)
matrix2 = np.random.randint(1, 11, (3,2))
print("matrix2:\n", matrix2)
arr10 = np.matmul(matrix1, matrix2)
print("10:\n", arr10)

arr11_1 = np.array([1, 2, 3, 4, 5])
arr11_2 = np.array([1, 2, 3, 4, 5])
if np.array_equal(arr11_1, arr11_2):
    print("11:\n", True)

arr12 = np.random.choice(range(1,21),10, replace=False)
print("12:\n", arr12)
max_index = np.argmax(arr12)
arr12[max_index] = 0
print("result:\n", arr12)

arr13 = np.array([1,2,3,4,5,5,6,7])
print("13:\n", arr13)
values, counts = np.unique(arr13, return_counts=True)
max_count_index = np.argmax(counts)
print("result:\n", values[max_count_index])

arr14 = np.random.randint(1, 10, 20)
print("14:\n", arr14)
n = int(input("Введите n: "))
result = np.partition(arr14, -n)[-n:]
print("result:\n", result)