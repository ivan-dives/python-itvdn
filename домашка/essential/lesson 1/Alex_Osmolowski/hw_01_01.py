# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __str__.


class Book:
    def __init__(self, author, title, public_year, genre):
        self.author = author
        self.title = title
        self.public_year = public_year
        self.genre = genre

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.author == other.author and \
               self.title == other.title and \
               self.public_year == other.public_year and \
               self.genre == other.genre

    def __ne__(self, other):
        if not isinstance(other, Book):
            return True
        return self.author != other.author or \
               self.title != other.title or \
               self.public_year != other.public_year or \
               self.genre != other.genre

    def __str__(self):
        __frm_tmpl = '"{}": автор - {}, год издания - {}, жанр - {}'
        return __frm_tmpl.format(self.title, self.author, self.public_year, self.genre)


def main():
    red_hen = Book("Шарль Перро", "Красная шапочка", 2012, "сказка")
    red_hen_copy = Book("Шарль Перро", "Красная шапочка", 2012, "сказка")
    buratino = Book("Алексей Толстой", "Золотой ключик или приключения Буратино", 2015, "сказка")

    print(red_hen)
    print(buratino)

    print(red_hen == red_hen_copy)
    print(red_hen != red_hen_copy)
    print(red_hen == buratino)
    print(red_hen != buratino)
    print(buratino == buratino)
    print(buratino != buratino)


if __name__ == '__main__':
    main()
