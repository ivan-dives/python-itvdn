#!/usr/bin/python3
# -*- coding: utf-8 -*-


def dec_even(fn):
    def wrap(*args, **kwargs):
        tmp = list(filter(lambda x: x % 2 == 0, fn(*args, **kwargs)))
        return tmp
    return wrap


@dec_even
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        a = b
        # b = a + b


for x in fib(10):
    print(x)

# x = fib(20)
# print(x)