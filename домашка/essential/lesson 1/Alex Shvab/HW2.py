class Book:

    def __init__ (self, author, name, year, ganre, comment = []):
        self.author = author
        self.name = name
        self.year = year
        self.ganre = ganre
        self.comment = comment


    def __str__(self):
        return f" Автор: {self.author}\n Книга: {self.name}\n " \
               f"Год написания: {self.year}\n Жанр: {self.ganre}\n " \
               f"Comments : {self.comment}"

class Comment:

    def __init__(self, human, comment):
        self.human = human
        self.comment = comment

    def __repr__(self):
        return f"{self.human}: {self.comment}"


comedy = Book("Данте", "Божественная комедия", 1308, "Эпос")
program = Book("Дональд Эрвин Кнут", "Искусство программирования", 1968, "Монография")
comedy.comment = [Comment("Вася", "Круто")]
program.comment = [
    Comment("Сашка", "Мало что понял но книга крутая"),
    Comment("Ваня", "Тяжко")]
print(comedy)
print()
print(program)