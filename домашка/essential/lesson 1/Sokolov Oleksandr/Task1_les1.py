class Book:

    def __init__(self, name, author, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"I read book - {self.author}, author's name \
- {self.name}, {self.year} year, genre - {self.genre}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    def __ne__(self, other):
            return not self.__eq__(other)

class Comment(Book):
    def __init__(self, comment, rayting):
        self.comment = comment
        self.rayting = rayting

book1 = Book('F Scott Fitzgerald', 'The Great Gatsby', 1923, 'Tragedy')
book1_copy = Book('F Scott Fitzgerald', 'The Great Gatsby', 1923, 'Tragedy')
book2 = Book('J. R. R. Tolkien', 'The Lord of the Rings', 1954, 'Fantasy')


print(book1)
print(book2)
print(book1 == book1_copy)
print(book1 != book1_copy)
print(book1 == book2)
print(book1 != book2)