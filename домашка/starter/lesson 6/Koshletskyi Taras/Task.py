#!/usr/bin/python3
# -*- coding: utf-8 -*_

from functools import lru_cache


class MyPolidron:

    def poli1(self, word):
        return word == word[::-1]

    def poli_reverse(self, word):
        return word == "".join(reversed(word))

    def poli_recurs(self, word):
        if len(word) < 2:
            return True
        if word[0] == word[-1]:
            return self.poli_recurs(word[1:-1])
        else:
            return False

    def poli_for(self, word):
        str = ''
        for i in range(len(word)):
            str += word[len(word) - 1 - i]
        return str == word


def sum(min, max):
    if max < min:
        return None
    elif max == min:
        return min
    else:
        return max+sum(min, max-1)


@lru_cache(maxsize=30)
def stairs(n):
    if n < 2:
        return 1
    return stairs(n-1) + stairs(n-2)


def main():
    a = MyPolidron()
    words = []
    with open("words.txt") as file:
        line = file.readline()
        while line:
            words.append(line.strip())
            line = file.readline()
        for word in words:
            print(f"{word}={a.poli1(word.lower())}", end=" ")
        print()
        for word in words:
            print(f"{word}={a.poli_reverse(word.lower())}", end=" ")
        print()
        for word in words:
            print(f"{word}={a.poli_for(word.lower())}", end=" ")
        print()
        for word in words:
            print(f"{word}={a.poli_recurs(word.lower())}", end=" ")
    print()
    print("Task Stairs")
    print(f'stairs = {stairs(40)}')
    print("Additional Task")
    print(f"sum = {sum(8,20)}")


if __name__ == '__main__':
    main()