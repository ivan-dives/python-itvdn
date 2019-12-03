#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Book:

    __reviews = []

    def __init__(self, author, title, years, genre):
        self.author = author
        self.title = title
        self.years = years
        self.genre = genre

    def __str__(self):
        return "This is book {} is " \
               "written by {} " \
               "in {} " \
               "and genre is {}".format(self.title, self.author, self.years, self.genre)

    def add_review(self, review):
        self.__reviews.append(review)

    def get_review(self):
        print(*self.__reviews)

    def get_author(self):
        return self.author

    def __eq__(self, other):
        return self.author == other.author \
               and self.title.lower() == other.title.lower() \
               and self.years == other.years \
               and self.genre.lower() == other.genre.lower()

