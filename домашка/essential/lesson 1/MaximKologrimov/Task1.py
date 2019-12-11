# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.

class Book:

    author = ''
    title = ''
    publishing = ''
    genre = ''

    def __init__(self, author_new, title_new, publishing_new, gener_new):
        self.author = author_new
        self.title = title_new
        self.publishing = publishing_new
        self.genre = gener_new

    def __str__(self):
        return f'Автор: {self.author}\n' \
               f'Название: {self.title}\n' \
               f'Год издания: {self.publishing}\n' \
               f'Жанр: {self.genre}'

    def __eq__(self, other):
        if self.author == other.author and \
           self.title == other.title and \
           self.publishing == other.publishing and \
           self.genre == other.genre:
            return f'{self.title} == {other.title} >>> {True}'
        else:
            return f'{self.title} == {other.title} >>> {False}'

    def __ne__(self, other):
        if self.title != other.title:
            return f'{self.title} != {other.title} >>> {True}'
        else:
            return f'{self.title} != {other.title} >>> {False}'
#__eq__
book1 = Book('Терри Вулф', 'The Kojima Code', '2019', 'Бестселлер')
book2 = Book('Ричард Морган', 'Сломленные ангелы', '2018', 'Фантастика')
book3 = Book('Дуглас Ричардс', 'Убийца Бога', '2015', 'Фантастика')
book4 = Book('Стивен Кинг', 'Доктор Сон', '2014', 'Триллер')
#__ne__
test1 = Book('Терри Вулф', 'The Kojima Code', '2019', 'Бестселлер')
test2 = Book('Терри Вулф', 'Кодзима - гений', '2019', 'Бестселлер')
test3 = Book('Терри Вулф', 'The Kojima Code', '0000', 'Бестселлер')

print(book1)
print()
print(book2)
print()
print(book3)
print()
print(book4)
print()


print(book1 == test1)
print(book1 == test2)
print()
print(book1 != test1)
print(book1 != test2)
print(book1 != test3)
