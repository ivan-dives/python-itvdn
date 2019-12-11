class Book:
    __author = ""
    __name = ""
    __year = 0
    __ganre = ""

    def __init__ (self, new_author, new_name, new_year, new_ganre):
        self.__author = new_author
        self.__name = new_name
        self.__year = new_year
        self.__ganre = new_ganre

    def __str__(self):
        return f" Автор: {self.__author}\n Книга: {self.__name}\n " \
               f"Год написания: {self.__year}\n Жанр: {self.__ganre}"

comedy = Book("Данте", "Божественная комедия", 1308, "Эпос")
print((comedy))
