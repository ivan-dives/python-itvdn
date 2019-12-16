#!/usr/bin/python3
# -*- coding: utf-8 -*_


text = "88 33 d fsfd 44 56 6y7 66 67  jj"


def foo(text):
    tmp = sorted([x for x in text.split() if x.isdigit()])
    # return string
    return ", ".join(x for x in tmp)


if __name__ == '__main__':
    print(foo(text))