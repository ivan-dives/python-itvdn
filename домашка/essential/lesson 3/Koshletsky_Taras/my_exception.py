#!/usr/bin/python3
# -*- coding: utf-8 -*_


class MyException(Exception):
    def __init__(self, message):

        super().__init__(message)


def main():
    try:
        raise MyException("CRASH")
    except MyException as error:
        print(error)


if __name__ == '__main__':
    main()