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

    def __eq__(self, other):
        if self.__author == other.__author and \
            self.__name == other.__name and \
            self.__year == other.__year and \
            self.__ganre == other.__ganre:
            return True
        else:
            return False



    def __str__(self):
        return f" Автор: {self.__author}\n Книга: {self.__name}\n " \
               f"Год написания: {self.__year}\n Жанр: {self.__ganre}"


comedy = Book("Данте", "Божественная комедия", 1308, "Эпос")
program = Book("Дональд Эрвин Кнут", "Искусство программирования", 1968, "Монография")
program2 = Book("Дональд Эрвин Кнут", "Искусство программирования", 1968, "Монография")
print(comedy)
print()
print(program)
print()
print(program == program2)
print(comedy != program)