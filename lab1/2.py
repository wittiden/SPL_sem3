russian_vowels = 'аеёиоуыэюя'
russian_consonants = 'бвгджзйклмнпрстфхцчшщ'

english_vowels = 'aeiouy'
english_consonants = 'bcdfghjklmnpqrstvwxz'

text = input("Введите текст: ").lower()
vowCount = 0
conCount = 0

for i in text:

     if i in russian_vowels or i in english_vowels:
         vowCount+=1
     elif i in russian_consonants or i in english_consonants:
         conCount+=1

print("Кол-во гласных = ", vowCount)
print("Кол-во согласных = ", conCount)
print("Всего", vowCount + conCount)

if vowCount == conCount:
    for i in text:
        if i in russian_vowels or i in english_vowels:
            print(i)