class Book:

    def __init__(self,author, book_title, year, genre_of_literature, review = 'По этой книге пока нет отзыва.'):
        self.author = author
        self.book_title = book_title
        self.year = year
        self.genre_of_literature = genre_of_literature
        self.review = review

    def __str__(self):
        return f'\nАвтор книги - {self.author}, Название книги -  {self.book_title} , Год выхода книги - {self.year}, Жанр - {self.genre_of_literature}.' \
                f'отзывы: {self.review} '

class Review:
    review = 'Пока нет отзывов'

    def __init__(self,review = review):
        self.review = review

    def __repr__(self):
        return f'Отзывы: {self.review}'


a = Book('Веллер', 'Майор звягин', '1991', 'Художественая')
b = Book('Джек Лондон', 'Сборник(Сила сильных)', '1914', 'Художественая' )
c = Book('Франко', 'Сотворение мира', '1905', 'Поема')

c.review = [Review('Неожидал такого от франка.')]
b.review = [Review('Долго не мог найти сборник сила сильных, спасибо вам.')]
print(a,b,c)
