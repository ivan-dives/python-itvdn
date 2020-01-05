#!/usr/bin/python3
# -*- coding: utf-8 -*_

import shelve

_URLS = shelve.open("link.db")


def add_link(link, short_link):

    if link in _URLS:
        print("Key is exist:", _URLS[link])
    else:
        _URLS[link] = short_link


def get_link(link):
    if link in _URLS:
        print(f"short link is {_URLS[link]}")
        return _URLS[link]
    else:
        print("Please create a link")


def find_link(short_link):

    if short_link in _URLS.values():
        for link, sh_link in _URLS.items():
            if short_link == sh_link:
                print(f"Link is: {link}")
                return link
    else:
        print("Short link doesn't exist")


def main():
    for k, v in enumerate(_URLS.items(), 1):
        print(k, v)

    # add_link("takoe", "siakoe")
    get_link("takoe")
    find_link("siakoe")



if __name__ == '__main__':
    main()