#!/usr/bin/python3
# -*- coding: utf-8 -*_


class A:

    def __init__(self, iter):
        self.iter = iter
        self.index = len(iter)

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.iter)

    def __next__(self):
        while True:
            try:
                if self.index == 0:
                    raise IndexError
                chr = self.iter[self.index-1]

            except IndexError:
                raise StopIteration
            self.index -= 1
            return chr


if __name__ == '__main__':
    str = "reversed"
    lst  = [x for x in range(0, 10)]
    gen = A(str)
    gen1 = A(lst)

    for i in gen:
        print(i, end=", ")
    print()
    for i in gen1:
        print(i, end=", ")