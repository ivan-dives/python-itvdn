#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            res = a / b
        except ZeroDivisionError as error:
            print(f"Catch an error: {error}")
            res = 0
        except TypeError as type_error:
            print(f"Catch an error: {type_error}")
            res = 0
        return res

    def exp(self, a, b):
        try:
            res = a**b
        except ZeroDivisionError as error:
            print(f"Catch an error: {error}")
            res = 0
        except TypeError as type_error:
            print(f"Catch an error: {type_error}")
            res = 0
        return res


def main():
    calc = Calculator()
    print(calc.division(5, 5))
    print(calc.division(5, 0))
    print(calc.division(5, "b"))
    print(calc.division(5, 5))
    print(calc.exp(0, -10))




if __name__ == '__main__':
    main()

