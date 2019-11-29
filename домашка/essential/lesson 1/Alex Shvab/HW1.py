class Book:

    def __init__ (self, author, name, year, ganre):
        self.author = author
        self.name = name
        self.year = year
        self.ganre = ganre

    def __eq__(self, other):
        if self.author == other.author and \
            self.name == other.name and \
            self.year == other.year and \
            self.ganre == other.ganre:
            return True
        else:
            return False



    def __str__(self):
        return f" Автор: {self.author}\n Книга: {self.name}\n " \
               f"Год написания: {self.year}\n Жанр: {self.ganre}"


comedy = Book("Данте", "Божественная комедия", 1308, "Эпос")
program = Book("Дональд Эрвин Кнут", "Искусство программирования", 1968, "Монография")
program2 = Book("Дональд Эрвин Кнут", "Искусство программирования", 1968, "Монография")
print(comedy)
print()
print(program)
print()
print(program == program2)
print(comedy != program)