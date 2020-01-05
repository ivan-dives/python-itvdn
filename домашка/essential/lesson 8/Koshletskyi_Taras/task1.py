#!/usr/bin/python3
# -*- coding: utf-8 -*_

# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
# Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.

import random
import os

lst = [random.randint(-1000000, 1000000) for _ in range(10000)]


def create_write(name):
    if os.path.exists(name):
        print("file exist")
        file = open(name, "w")
    else:
        print("Create File")
        file = open(name, "x")
    for number in lst:
        file.write(f"{number}\n")


def read(path):
    sum = 0
    count = 0
    with open(path) as file:
        for line in file:
            sum +=int(line)
            count +=1
    print(sum/count)
    return sum/count


def main():
    print(len(lst))
    # print(os.getcwd())
    create_write("test.txt")
    read("test.txt")


if __name__ == '__main__':
    main()

