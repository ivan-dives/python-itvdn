#!/usr/bin/python3
# -*- coding: utf-8 -*_

import random

# lst = [random.randint(1, 1000) for j in range(1, 10)]
lst = [10, 9, 8, 7, 1, 2, 3, 4, 5]
print(lst)


for i in range(0, len(lst)):
    for j in range(0, len(lst) - 1):
        if lst[j] > lst[j+1]:
            tmp = lst[j+1]
            lst[j + 1] = lst[j]
            lst[j] = tmp

print(lst)