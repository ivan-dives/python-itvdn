class Book:
    author = 'unknown'
    book_title = 'unknown'
    year = 'unknown'
    genre_of_literature = 'unknown'

    def __init__(self,author, book_title, year, genre_of_literature):
        self.author = author
        self.book_title = book_title
        self.year = year
        self.genre_of_literature = genre_of_literature

    def __str__(self):
        return f'\nАвтор книги - {self.author}, Название книги -  {self.book_title} , Год выхода книги - {self.year}, Жанр - {self.genre_of_literature}.'

a = Book('Веллер', 'Майор звягин', '1991', 'Художественая')
b = Book('Джек Лондон', 'Сборник(Сила сильных)', '1914', 'Художественая' )
c = Book('Франко', 'Сотворение мира', '1905', 'Поема')
print(a,b,c)