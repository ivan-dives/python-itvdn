class Book:

   def __init__(self, author, name, year, genre, rew = []):
       self.author = author
       self.name = name
       self.year = year
       self.genre = genre
       self.rew = rew

   def __str__(self):
       return f"I read book - {self.author}, author's name - {self.name}, {self.year} year, genre - {self.genre}, Commemts - {self.rew}"

class Comen:

   def __init__(self, rew):
       self.rew = rew

   def __repr__(self):
       return f"Good: {self.rew}"

book1 = Book("F Scott Fitzgerald", "The Great Gatsby", 1923, "Tragedy")
book1.rew = [Comen("Recommend book, read twice")]
print()
print(book1)