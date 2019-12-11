#!/usr/bin/python3
# -*- coding: utf-8 -*_


def rev(lst):
    size = len(lst)

    while size != 0:
         chr = lst[size-1]
         yield chr
         size -=1


if __name__ == '__main__':
    str = "reversed"
    lst  = [x for x in range(0, 10)]
    gnr = rev(str)
    gnr1 = rev(lst)
    gnr2 = rev(lst)


    for i in gnr:
        print(i, end=", ")
    print()
    for i in gnr1:
        print(i, end=", ")
    print()

print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))
print(next(gnr2))