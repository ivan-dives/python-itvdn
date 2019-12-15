#!/usr/bin/python3
# -*- coding: utf-8 -*_


def average(*args):
    return sum(args)/len(args)


if __name__ == '__main__':
    lst = [x for x in range(10)]
    print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
    print(average(*lst))
