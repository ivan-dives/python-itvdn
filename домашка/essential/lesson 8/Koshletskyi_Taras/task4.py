#!/usr/bin/python3
# -*- coding: utf-8 -*_

# Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.

import json
import os
import time
import pickle

items = [{
    "apple": 100,
    "pineapple": 50,
    "orange":300,
}]


def make_json(path, items):
    with open(path, "w") as file:
        json.dump(items, file)


def read_json(path):
    with open(path) as file:
        data = json.load(file)
    print(data)


def make_pickle(path, items):
    with open(path, "wb") as file:
        pickle.dump(items, file)


def read_pickle(path):
    with open(path, "rb") as file:
        data = pickle.load(file)
    print(data)

def main():
    make_json("json.json", items)
    read_json("json.json")
    make_pickle("pic.bin", items)
    read_pickle("pic.bin")
    # time.sleep(10)
    # os.remove("json.json")
    # print("Remove file")


if __name__ == '__main__':
    main()
