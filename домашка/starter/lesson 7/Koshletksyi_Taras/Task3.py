#!/usr/bin/python3
# -*- coding: utf-8 -*_

import math

CHOICE = ["sum", "multiplication"]

def makeList(n):
    return [i for i in range(1, n+1)]


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


def findNumbers(lst):
    simleLst = []
    for i in lst:
        if is_prime(i):
            simleLst.append(i)
    return simleLst

def main():
    lst = makeList(300)
    simpleNumber = findNumbers(lst)
    print(simpleNumber)
    ch = input("Make a choice sum/multiplication").lower()
    if ch in CHOICE:
        if ch == "sum":
            print(sum(simpleNumber))
        else:
            mult = 1
            for i in range(0, len(simpleNumber)-1):
                mult *= simpleNumber[i]
            print(mult)

if __name__ == '__main__':
    main()

