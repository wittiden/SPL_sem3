import os
try:
    file1 = open('f1.txt','w')
    flag = True

    while flag:
        data = input('Вводите информацию: ')
        if data == '':
            flag = False
        file1.write(data + '\n')

    file1.close()
except IOError:
    print('File not found')

try:
    file2 = open('f2.txt','w')
    file1 = open('f1.txt','r')

    line_count = 0
    for line in file1:
        if line_count < 4:
            file2.write(line)
            line_count += 1
        else:
            break

    file1.close()
    file2.close()
except IOError:
    print('File not found')

try:
    size1 = os.path.getsize('f1.txt')
    size2 = os.path.getsize('f2.txt')
    print(size1, size2)
except OSError:
    print('File not found')