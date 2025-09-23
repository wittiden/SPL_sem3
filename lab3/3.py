file = open("study.txt", 'r', encoding='utf-8')

subject_dict = {}
for line in file:
    line = line.strip()

    subject, numbers_part = line.split(':', 1)
    subject = subject.strip()

    total = 0
    for word in numbers_part.split():
        if '(' in word:
            number_str = word.split('(')[0]
        else:
            number_str = word

        if number_str.isdigit():
            total += int(number_str)

    subject_dict[subject] = total

print(subject_dict)
file.close()