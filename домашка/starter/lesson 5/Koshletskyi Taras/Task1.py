#!/usr/bin/python3
# -*- coding: utf-8 -*_


def greeting(name="Taras"):
    print(f"Hello {name}")


def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return  a * b


def division(a, b):
    if a == 0 or b == 0:
        return "Division by zero"
    return a/b


def average(a, b, c):
    return (a + b + c)/3


def main():
    greeting()
    while True:
        a = input("Input a: ").strip()
        if a.isdigit():
            a = int(a)
        elif a.lower() == "quit":
            break
        b = input("Input b: ").strip()
        if b.isdigit():
            b = int(b)
        elif b.lower() == "quit":
            break
        func = input("Please input name of func add / subtraction / multiplication / division ").strip()
        if func.lower() == "quit":
            break
        elif func.lower() == "add":
            print(add(a, b))
        elif func.lower() == "subtraction":
            print(subtraction(a, b))
        elif func.lower() == "multiplication":
            print(multiplication(a, b))
        elif func.lower() == "division":
            print(division(a, b))

    a, b, c = map(int, input('a = _, b = _, c = _').strip().split())
    print(average(a, b, c))


if __name__ == '__main__':
    main()
