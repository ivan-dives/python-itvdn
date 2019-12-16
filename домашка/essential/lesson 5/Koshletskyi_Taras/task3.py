#!/usr/bin/python3
# -*- coding: utf-8 -*_

import string

text = "An article is a word used to modify a noun, which is a person, place, object, or idea. Technically, an article " \
       "is an adjective, which is any word that modifies a noun. Usually adjectives modify nouns through description, " \
       "but articles are used instead to point out or refer to nouns."


def sort_test(text):
    tmp = text.translate(text.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    lst = tmp.split()
    print(sorted(lst, key=str.casefold))


if __name__ == '__main__':
    sort_test(text)