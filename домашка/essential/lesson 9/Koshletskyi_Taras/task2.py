#!/usr/bin/python3
# -*- coding: utf-8 -*-


import random

lst = [random.randint(1, 10) for _ in range(20)]
print(lst)
lst2 =list(map(lambda x: x **2, list(filter(lambda x: x % 2 != 0, lst))))
print(lst2)