class Book:
    review = ''
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre



    # def __repr__(self):
    #     return "Book".format(self.name, self.author, self.year, self.genre)
    def __str__(self):
        return "The Book named {}, writen by the {} at {} in {} genre".format(self.name, self.author, self.year, self.genre)

    def print_info(self):
        print(self.name, self.author, self.year, self.genre)
        print(self.review)
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.year == other.year and self.genre == other.genre
    def __ne__(self, other):
        return self.name != other.name and self.author != other.author and self.year != other.year and self.genre != other.genre

    class Comment:

        def __init__(self, review):
            self.review = review
        def __str__(self):
            return "\n".format(self.review)
        def print_review(self):
            print(self)

        @classmethod
        def from_book(cls, book, comment=None):
            review = (book.name + book.author + book.year + book.genre + comment.review)
            return cls(review)
# def main():
#     book = Book(name, author, year, genre)
#     new_review = Comment.from_book(book)
#     print(new_review)
#
# if __name__ == '__main__':
#     main()
    
alice = Book("Alice in wonderlad", "Lewis Carroll", 1865, "fairytale")
alice.review = """\nСказка Алиса в стране чудес, о приключениях девочки Алисы в воображаемом мире. 
Чарльз Лютвидж Доджсон в 1865 году, под псевдонимом Льюис Кэрролл, 
издал впервые эту необычную сказку, свершившую переворот в жанре фантастики. 
Сказка Алиса в стране чудес славится своими философскими шутками и игрой слов. 
Чеширский кот, Белый кролик, Мартовский Заяц, Шляпник и другие персонажи стали культовыми, 
а сценки из сказки, такие, как, Безумное чаепитие - предметом споров и многочисленных разгадок загадки, 
которую Льюис Кэрролл и не принимал всерьёз.\n"""
print(Book("Alice in wonderlad", "Lewis Carroll", 1865, "fairytale"))
print(alice.review)

flat_world = Book("Flat world", "Terry Pratchet", 1983, "fantasy")
flat_world.review = """\nМир, описанный автором совершенно непредсказуем: в радуге целых 8 цветов, в неделе 8 дней, 
как и времен года, их тоже 8. Эта цифра обладает большой энергией, она магическая и ее нельзя называть вслух. 
Так называемый Плоский мир находится на четырех слонах, что стоят на панцире черепахи, движущейся по Космосу. 
Здесь магия вполне себе материальна, а свет движется плавно и медленно. 
Жители, как можно догадаться, также весьма нетипичные.\n"""
print(Book("Flat world", "Terry Pratchet", 1983, "fantasy"))
print(flat_world.review)

dark_tower = Book ("Dark tower", "Stephen King",1982, "triller" )
dark_tower.review = """\nТемная башня" Стивена Кинга, это эпический семитомник о похождениях Роланда Дискейна из Гелиада, 
последнего стрелка. Кинг писал ее около 30-и лет. Отразил в книгах многие события из своей жизни, и появился в ней сам.\n"""
print(Book("Dark tower", "Stephen King",1982, "triller" ))
print(dark_tower.review)

enciclopedy = Book ("Big soviet enciclopedy", "many authorth", 1969,"science")
enciclopedy.review = """\nнаиболее известная и полная советская универсальная энциклопедия. 
Выпускалась с 1926 года (первый том первого издания) по 1990 год (последний ежегодник) 
издательством «Советская энциклопедия» (ныне — издательство «Большая Российская энциклопедия»).\n"""
print(Book("Big soviet enciclopedy", "many authorth", 1969,"science"))
print(enciclopedy.review)

print(flat_world == dark_tower)



