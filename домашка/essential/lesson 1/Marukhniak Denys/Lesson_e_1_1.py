# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, метод __str__.


class Book:
    authors_name = '-'
    name = '-'
    year_of_publication = '-'
    genre = '-'

    def __init__(self, new_authors_name, new_name, new_publication, new_genre):
        self.authors_name = new_authors_name
        self.name = new_name
        self.year_of_publication = new_publication
        self.genre = new_genre

    def __str__(self):
        return f"Author's name: {self.authors_name}\n" \
               f"Name of the book: {self.name}\n" \
               f"Year of publication: {self.year_of_publication}\n" \
               f"Genre of book: {self.genre}"

    def __eq__(self, other):
        if self is self.name:
            print(f'{self.name} is {other.name}?')
            return self.name is other.name
        elif self is self.authors_name:
            print(f'{self.authors_name} == {other.authors_name}?')
            return self.authors_name is other.authors_name

    def __ne__(self, other):
        print(f'"{self.name}" is not "{other.name}"?')
        return self.name is not other.name


a = Book('Виктор Пелевин', 'Чапаев и Пустота', '1996', 'Фантастика')
b = Book('Стивен Кинг', 'Сияние', '1977', 'Ужасы')
c = Book('Стивен Кинг', 'Зелёная миля', '1996', 'Фэнтези')

print(a)
print('----------------------------------')
print(b)
print('----------------------------------')
print(c)
print('----------------------------------')

print(a == b)
print(a.authors_name == b.authors_name)
print(a != b)
