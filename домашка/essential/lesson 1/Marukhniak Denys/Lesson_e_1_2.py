# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


class Review:
    new_review = []

    def __init__(self, text):
        self.new_review = [text]


class Book:
    authors_name = 'Отсутствует'
    name = 'Отсутствует'
    year_of_publication = 'Отсутствует'
    genre = 'Отсутствует'
    reviews = []

    def new_review(self, text):
        new_review = Review(text)
        self.reviews.append(new_review)

    def __init__(self, new_authors_name, new_name, new_publication, new_genre):
        self.authors_name = new_authors_name
        self.name = new_name
        self.year_of_publication = new_publication
        self.genre = new_genre

    def __str__(self):
        return f"Author's name: {self.authors_name}\n" \
               f"Name of the book: {self.name}\n" \
               f"Year of publication: {self.year_of_publication}\n" \
               f"Genre of book: {self.genre}\n" \
               f"Reviews: {self.reviews}"

    def __eq__(self, other):
        print(f'"{self.name}" is "{other.name}"?')
        return self.name is other.name

    def __ne__(self, other):
        print(f'"{self.name}" is not "{other.name}"?')
        return self.name is not other.name


id_b = [[], [], []]
id_b[0] = Book('Виктор Пелевин', 'Чапаев и Пустота', '1996', 'Фантастика')
id_b[1] = Book('Стивен Кинг', 'Сияние', '1977', 'Ужасы')
id_b[2] = Book('Стивен Кинг', 'Зелёная миля', '1996', 'Фэнтези')
id_b[1].reviews = ['Норм']
id_b[2].reviews = ['Щедевр', '10 изи 10']

while True:
    yes_no = input('Хотите ввести отзыв для книги (Y/S)? ')
    if yes_no.lower() == 'y':
        id_num = int(input('Введите id книги, которой хотите оставить отзыв: '))
        review = input('Введите отзыв: ')
        id_b[id_num].new_review(review)
    elif yes_no.lower() == 'n':
        break

print('----------------------------------')
print(id_b[0])
print('----------------------------------')
print(id_b[1])
print('----------------------------------')
print(id_b[2])
print('----------------------------------')

print(id_b[0] == id_b[1])
print(id_b[0] != id_b[1])

