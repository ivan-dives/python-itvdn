#!/usr/bin/python3
# -*- coding: utf-8 -*_

import random


def fill_list(n):
    list =[]
    for i in range(0, n):
        while True:
            if random.randint(0, 1000) not in list:
                list.append(random.randint(0, 1000))
                break
    return list


def maximum(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max


def minimum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min


def average(list):
    sum = 0
    for i in list:
        sum +=i

    return sum / len(lst)


if __name__ == '__main__':
    lst = fill_list(100)
    print(maximum(lst))
    print(minimum(lst))
    print(average(lst))
    print(max(lst) == maximum(lst))
    print(min(lst) == minimum(lst))
