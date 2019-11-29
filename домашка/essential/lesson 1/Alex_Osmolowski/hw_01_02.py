# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


class Book:
    def __init__(self, author, title, public_year, genre):
        self.author = author
        self.title = title
        self.public_year = public_year
        self.genre = genre
        self.comments = []

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
        frm_tmpl = '"{}": автор - {}, год издания - {}, жанр - {}'
        ttl = frm_tmpl.format(self.title, self.author, self.public_year, self.genre)
        if self.comments:
            for cmt in self.comments:
                ttl += "\n\n" + str(cmt)
        return ttl


class Comment(object):
    def __init__(self, comment_author, text):
        self.comment_author = comment_author
        self.text = text

    def __str__(self):
        return self.comment_author+":\n"+self.text


def main():
    red_hen = Book("Шарль Перро", "Красная шапочка", 2012, "сказка")
    red_hen.comments.append(Comment("Дюймовочка", "Замечательная детская книжка"))
    red_hen.comments.append(Comment("Пошляк",
                                    "Красная шапочка гуляла в лесу одна потому, что лес она знала, а секс любила."))
    buratino = Book("Алексей Толстой", "Золотой ключик или приключения Буратино", 2015, "сказка")

    print(red_hen)
    print()
    print()
    print(buratino)


if __name__ == '__main__':
    main()
