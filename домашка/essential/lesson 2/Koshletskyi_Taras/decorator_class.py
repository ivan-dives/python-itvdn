#!/usr/bin/python3
# -*- coding: utf-8 -*_


class MyDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self):
        print("*" * 30)
        self.function()
        print("*" * 30)


@MyDecorator
def foo():
    print("This is foo")


if __name__ == '__main__':
    foo()
