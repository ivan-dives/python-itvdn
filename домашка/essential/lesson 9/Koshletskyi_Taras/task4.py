#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functools

def mul(a, b):
    return a * b

x = functools.partial(mul, 5)
print(x(10))
print(x(20))


def cur_mul(x):
    def inner_mul(y):
        return x * y
    return inner_mul

q = cur_mul(10)
print(q(20))
print(q(2))


t = mul(6)
print(t(7))