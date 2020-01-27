class WordSequence(list):
    _delimiters = ('.', ',', ';', ':', ' -', '- ')

    def __init__(self, text):
        words = [word.casefold() for word in WordSequence._split(text)]
        for word in words:
            if word not in self:
                self.append(word)

    def _split(text):

        string = text
        for delimiter in WordSequence._delimiters:
            string = string.replace(delimiter, ' ')
        return string.split()


def main():
    texxt = input('Введите текст с клавиатуры: ')

    words = WordSequence(texxt)
    for word in sorted(words):
        print(word)


if __name__ == '__main__':
    main()
