#!/usr/bin/python3
# -*- coding: utf-8 -*_

# Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными файлами.


import random
import os

lst = [random.randint(-1000000, 1000000) for _ in range(10000)]


def create_write(name):
    if os.path.exists(name):
        print("file exist")
        file = open(name, "wb")
    else:
        print("Create File")
        file = open(name, "xb")
    for num in lst:
        file.write(bytes(str(num)+" ", "utf-8"))


def read(path):
    size = os.path.getsize(path)
    sum = 0
    count = 0
    with open(path, "rb") as file:
        data = file.read()
        lst = data.split()
        for num in lst:
            sum += int(num)
            count += 1
    print(sum/count)


def main():
    print(len(lst))
    # print(os.getcwd())
    create_write("test.bin")
    read("test.bin")


if __name__ == '__main__':
    main()
