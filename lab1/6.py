import string

text = input("Введите текст для преобразования: ")

text = text.translate(str.maketrans('', '', string.punctuation))
text = tuple(text.split())
print(text)