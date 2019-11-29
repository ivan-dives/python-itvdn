#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Review:

    def __init__(self, review=None):
        self.review = review

    def __str__(self):
        if self.review:
            return self.review
        else:
            return "No review on this book"


class Book:


    def __init__(self, author, title, years, genre, review=None):
        self.author = author
        self.title = title
        self.years = years
        self.genre = genre
        self.__rev = review


    def __str__(self):
        return "This is book {} is " \
               "written by {} " \
               "in {} " \
               "and genre is {} and review: {}".format(self.title, self.author, self.years, self.genre , self.__rev)


rev = Review()
rev1 = Review("Good")

book = Book("Tolstoy", "WAR", "1488", "Mystic", rev)
book1 = Book("Hydoi", "Peasw", "740", "Takoe", rev1)
print(book)
print(book1)

