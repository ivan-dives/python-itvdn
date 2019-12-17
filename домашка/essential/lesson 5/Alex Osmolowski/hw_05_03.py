# Задание 3
# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
# данного текста.


class WordsSet(list):
    """Класс, представляющий множество слов"""

    __delims = ('.', ',', ';', ':', ' -', '- ', "!", "?")

    def __init__(self, text):
        super().__init__()
        words = [word.casefold() for word in WordsSet.__split(text)]
        for word in words:
            if word not in self:
                self.append(word)

    @staticmethod
    def __split(text):
        """Метод разбиения текста."""
        string = text
        for delim in WordsSet.__delims:
            string = " ".join(string.split(delim))
        return string.split()


def main():
    print("Введите ваш текст:")
    text = input()
    words = WordsSet(text)
    for word in sorted(words):
        print(word)


if __name__ == '__main__':
    main()