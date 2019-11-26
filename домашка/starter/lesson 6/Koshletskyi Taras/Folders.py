#!/usr/bin/python3
# -*- coding: utf-8 -*_

import os
import pathlib

PATH = pathlib.Path('/Users/taraskoshletskyi/Downloads/test')


def tree(path):
    if not os.path.exists(path):
        print("Path is not exist")
        return
    if len(os.listdir(path)) == 0:
        print(path)
    for i in os.listdir(path):
        if os.path.isfile(path/i):
            print(path / i)
        elif os.path.isdir(path / i):
            tree(path / i)


if __name__ == '__main__':
    tree(PATH)

