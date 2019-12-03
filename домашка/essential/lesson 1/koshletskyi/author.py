#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Author:

    __books = []

    def __init__(self, name, surname, birth, death=None):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.death = death

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        print(*self.__books)

    def __str__(self):
        return f'Hello my name is {self.name} {self.surname},I was burn in {self.birth} and I have {len(self.__books)} books'

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() \
        and self.surname.lower() == other.surname.lower() \
        and self.birth == other.birth
