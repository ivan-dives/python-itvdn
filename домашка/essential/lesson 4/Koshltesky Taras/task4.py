#!/usr/bin/python3
# -*- coding: utf-8 -*_

import math


def simple_number(number):
    yield from (i for i in range(number) if is_prime(i))


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = math.sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':

    for i in simple_number(10000):
        print(i, end=", ")
    print()
    f = simple_number(10)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
