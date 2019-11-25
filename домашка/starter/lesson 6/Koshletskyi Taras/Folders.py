#!/usr/bin/python3
# -*- coding: utf-8 -*_

import os

path = '/Users/taraskoshletskyi/Downloads'


def tree(path):
    if not os.path.exists(path):
        print("Path is not exist")
        return
    if len(os.listdir(path)) == 0:
        print(path)
    for i in os.listdir(path):
        if os.path.isfile(f'{path}/{i}'):
            print(f'{path}/{i}')
        elif os.path.isdir(f'{path}/{i}'):
            tree(f'{path}/{i}')


if __name__ == '__main__':
    tree(path)

