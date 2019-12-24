# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте
# отдельные его имена.


import sys
import os
import pathlib

pt = pathlib.Path(os.getcwd()+'/../../lesson 4/Alex Osmolowski/').resolve()
# print(pt)
sys.path.insert(0, pt)
# print(sys.path[0])
from hw_04_add import *


def main():
    while True:
        k = input("Введите требуемое количество простых чиcел (целое положительное число): ")
        try:
            k = int(k)
        except TypeError:
            continue
        if k < 1 :
            continue
        break

    for i in simple_gen(k):
        print(i, end="  ")


if __name__ == '__main__':
    main()