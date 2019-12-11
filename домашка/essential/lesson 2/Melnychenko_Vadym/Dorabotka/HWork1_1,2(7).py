import copy
class Kniga():

    def __init__(self, author, nazvanie, year, genre):
        self.author = author
        self.nazvanie = nazvanie
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.author == other.author and \
            self.nazvanie == other.nazvanie and \
            self.year == other.year and \
            self.genre == other.genre

    def __str__(self):
        return f'Книга "{self.nazvanie}" писателя {self.author} ' \
               f'(издана в {self.year} году, жанр книги: {self.genre})'


class Comment():
    def __init__(self, ot_kogo, chto_n):
        self.ot_kogo = ot_kogo
        self.chto_n = chto_n

    def __str__(self):
        return f'{self.ot_kogo}, {self.chto_n}'


kniga = Kniga('Ivan Ivanych', 'Python', 2000, 'Ivanishino')
kniga2 = copy.copy(kniga)
kniga3 = Kniga('Ivan Ivanych2', 'Python', 2011, 'Ivanishino2')

print(f'Книга: {kniga}')
print(f'Книга: {kniga3}')
kom = input('Вы хотите ввести комент (y/n):')

if kom.lower() == 'y':
    x = input('Введите свое имья: ')
    z = input('Введите коментарий для книги: ')
    y = int(input('К какой книге добавить комент (1, 2): '))
    comments = Comment(x, z)
    if y == 1:
        print(kniga)
        print(comments)
    elif y == 2:
        print({kniga})
        print(comments)
    else:
        pass
else:
    pass

print(kniga == kniga2)
print(kniga != kniga3)
