from tkinter.scrolledtext import example


class Alphabet:
    def __init__(self, lang = None, letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"):
        self.__lang = lang
        self.letters = letters
    def print_alphabet(self):
        for letter in self.letters:
            print(letter, end=" ")
    def letters_num(self):
        print(f'\n {len(self.letters)}')

class EngAlphabet(Alphabet):
    def __init__(self, lang = None, letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", eng_letters  = "abcdefghijklmnopqrstuvwxyz"):
        super().__init__(lang, letters)
        self.__eng_letters = eng_letters
    def print_alphabet(self):
        for letter in self.__eng_letters:
            print(letter, end=" ")
    def is_en_letter(self, newLetter):
        find = False
        for letter in self.__eng_letters:
            if newLetter.lower() == letter.lower():
                find = True
                return print(True)
        if not find:
            print(False)
        return None
    def letters_num(self):
        print(f'\n {len(self.__eng_letters)}')

    @staticmethod
    def example():
        print("First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple.")

obj1 = Alphabet()
obj1.print_alphabet()
obj1.letters_num()

print("\n")

obj2 = EngAlphabet()
obj2.print_alphabet()
obj2.letters_num()

print("\n")

newLetter = input("Введите букву: ")
obj2.is_en_letter(newLetter)

print("\nПример текста на английском: ")
obj2.example()