#!/usr/bin/python3
# -*- coding: utf-8 -*_

from functools import lru_cache


class MyPolidron:

    def poli1(word):
        return word == word[::-1]

    def poli_reverse(word):
        return word == "".join(reversed(word))

    def poli_recurs(word):
        if len(word) < 2:
            return True
        if word[0] == word[-1]:
            return MyPolidron.poli_recurs(word[1:-1])
        else:
            return False

    def poli_for(word):
        str = ''
        for i in range(len(word)):
            str += word[len(word) - 1 - i]
        return str == word


def sum(min, max):
    if max < min:
        return None
    elif max == min:
        return min
    elif:
        return max+sum(min, max-1)


@lru_cache(maxsize=30)
def stairs(n):
    if n < 2:
        return 1
    return stairs(n-1) + stairs(n-2)


def main():
    words = []
    with open("words.txt") as file:
        for line in file.readline.strip():
            words.append(line)

        #line = file.readline().strip()
        #while line:
        #    words.append(line)
        #    line = file.readline().strip()
    function = [fun for fun in dir(MyPolidron) if not fun.startswith("_")]
    for fun in function:
        print(f"{fun}: ", end="")
        for word in words:
            method_to_call = getattr(MyPolidron, fun)
            print(f"{word}={method_to_call(word.lower())}", end=" ")
        print()
    print("Task Stairs")
    print(f'stairs = {stairs(40)}')
    print("Additional Task")
    print(f"sum = {sum(8,20)}")


if __name__ == '__main__':
    main()