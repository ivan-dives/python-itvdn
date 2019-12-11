# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class Book:
    author = ''
    title = ''
    publishing = ''
    genre = ''
    rev = []

    def __init__(self, author_new, title_new, publishing_new, gener_new, rev_list=[]):
        self.author = author_new
        self.title = title_new
        self.publishing = publishing_new
        self.genre = gener_new
        self.rev = rev_list

    def __str__(self):
        return f'Автор: {self.author}\n' \
               f'Название: {self.title}\n' \
               f'Год издания: {self.publishing}\n' \
               f'Жанр: {self.genre}\n' \
               f'Отзыв: {self.rev}'

book3 = Book('Дуглас Ричардс', 'Убийца Бога', '2015', 'Фантастика')
book4 = Book('Стивен Кинг', 'Доктор Сон', '2014', 'Триллер')


class Reviews:

    def __init__(self, rev_new):
        self.rev = rev_new

    # def __str__(self):
    #     return f'anonymous: {self.rev}\n'

    def __repr__(self):
        return f'anonymous: {self.rev}'


rev3_1 = Reviews('Купив у подарунок сестрі. За її словами одна з найкращих книг Кінга, тому можете купувати')
rev3_2 = Reviews('Продолжение известно-экранизированного романа «Сияние»')
rev3_3 = Reviews('Книга учит думать. Кинг, как и всегда, непревзойденный')
rev4_1 = Reviews('На мой взгляд книга получилась немного растянутой')
rev4_2 = Reviews('Глубокие философские размышления в купе с космической темой и темой сверх разума')
rev4_3 = Reviews('Ощутимо лучше первого романа')

list = [rev3_1, rev3_2, rev3_3, rev4_1, rev4_2, rev4_3]


# for book3.rev in list[:3]:
#     print(f'{book3}\n')
#
# for book4.rev in list[3:]:
#     print(f'{book4}\n')

book3.rev = list[:3]
book4.rev = list[3:]
print(book3)
print()
print(book4)