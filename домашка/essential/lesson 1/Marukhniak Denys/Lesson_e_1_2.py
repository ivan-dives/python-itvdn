# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


class Reviews:
    def __init__(self, reviews=None):
        if reviews is None:
            reviews = []
        self.reviews = reviews

    def add_review(self, text):
        self.reviews.append(text)

    def __str__(self):
        if self.reviews:
            return f"Reviews: {self.reviews}"
        else:
            return 'Book has no reviews'


class Book:
    def __init__(self, authors_name, name, publication, genre):
        self.authors_name = authors_name
        self.name = name
        self.year_of_publication = publication
        self.genre = genre

    def __str__(self):
        return f"Author's name: {self.authors_name}\n" \
               f"Name of the book: {self.name}\n" \
               f"Year of publication: {self.year_of_publication}\n" \
               f"Genre of book: {self.genre}\n"

    def __eq__(self, other):
        print(f'"{self.name}" is "{other.name}"?')
        return self.name is other.name

    def __ne__(self, other):
        print(f'"{self.name}" is not "{other.name}"?')
        return self.name is not other.name


id_b = [
    Book('Виктор Пелевин', 'Чапаев и Пустота', '1996', 'Фантастика'),
    Book('Стивен Кинг', 'Сияние', '1977', 'Ужасы'),
    Book('Стивен Кинг', 'Зелёная миля', '1996', 'Фэнтези'),
]
id_r = [Reviews(), Reviews(), Reviews()]
while True:
    yes_no = input('Хотите ввести отзыв для книги (Y/N)? ')
    if yes_no.lower() == 'y':
        id_num = int(input('Введите id книги, которой хотите оставить отзыв: '))
        review = input('Введите отзыв: ')
        id_r[id_num].add_review(review)
    elif yes_no.lower() == 'n':
        break

print('----------------------------------')
print(id_b[0], id_r[0], sep='')
print('----------------------------------')
print(id_b[1], id_r[1], sep='')
print('----------------------------------')
print(id_b[2], id_r[2], sep='')
print('----------------------------------')
print(id_b[0] == id_b[1])
print(id_b[0] != id_b[1])
