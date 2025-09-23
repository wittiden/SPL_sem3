try:
    averageSalary = 0
    count = 0
    file = open('salary.txt', 'r')
    for line in file:
        parts = line.split()
        salary = float(parts[-1])
        averageSalary += salary
        count += 1
        if salary < 20000:
            print(line.strip())

    print(averageSalary/count)
except FileNotFoundError:
    print('No such file')
except IOError:
    print('Error reading file')