#!/usr/bin/python3
# -*- coding: utf-8 -*_


lst = [i for i in range(0, 10)]
print(lst)
lst.reverse()
print(lst)

new_lst = []
for i in lst:
    new_lst.append(lst[len(lst)-i-1])

print(new_lst)

new_new_lst = new_lst[::-1]

print(new_new_lst)