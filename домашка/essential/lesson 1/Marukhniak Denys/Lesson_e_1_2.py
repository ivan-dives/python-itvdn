# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


class Review:
    reviews = []

    def __init__(self, text):
        self.reviews = text

    def add_review(self, text):
        self.reviews.append(text)

    def __str__(self):
        return f"Reviews: {self.reviews}"


class Book(Review):

    def __init__(self, new_authors_name, new_name, new_publication, new_genre):
        self.authors_name = new_authors_name
        self.name = new_name
        self.year_of_publication = new_publication
        self.genre = new_genre

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
    Book('Стивен Кинг', 'Зелёная миля', '1996', 'Фэнтези')
]

id_r = [Review('Норм'), Review('Щедевр')]

while True:
    yes_no = input('Хотите ввести отзыв для книги (Y/N)? ')
    if yes_no.lower() == 'y':
        id_num = int(input('Введите id книги, которой хотите оставить отзыв: '))
        review = input('Введите отзыв: ')
        id_r[id_num].add_review(review)
    elif yes_no.lower() == 'n':
        break

print('----------------------------------')
print(id_b[0], id_r[0])
print('----------------------------------')
print(id_b[1], id_r[1])
print('----------------------------------')
print(id_b[2], id_r[2])
print('----------------------------------')
print(id_b[0] == id_b[1])
print(id_b[0] != id_b[1])
