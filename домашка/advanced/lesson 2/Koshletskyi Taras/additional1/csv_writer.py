#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import json
from xml.etree import ElementTree
from xml.dom import minidom

# Создайте функцию, которая будет создавать CSV файл на основе данных, введенных пользователем через консоль.
# Файл должен содержать следующие колонки: имена, фамилии, даты рождений и город проживания.
# Реализовать возможности перезаписи данного файла, добавления новых строк в существующий
# файл, построчного чтения из файла и конвертацию всего содержимого в форматы XML и JSON


def _input_data():
    first_name = input("Input name:")
    last_name = input("Input surname:")
    date = input("Input date of birthday:")
    city = input("Input city:")
    user = {
            "first_name": first_name,
            "last_name": last_name,
            "date": date,
            "city": city,
        }
    return user


def write_to_file(path, mode="w"):
    users = []
    n = 0
    while n != 1:
        print("To Exit input ---> allah")
        users.append(
            _input_data())
        n += 1
    with open(path, mode) as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'date', 'city'])
        if mode == "w":
            writer.writeheader()
        for user in users:
            writer.writerow(user)


def add_to_file(path):
    write_to_file(path, "a")


def read_file(path):
    with open(path) as file:
        reader = csv.DictReader(file, fieldnames=['first_name', 'last_name', 'date', 'city'])
        line = next(reader)
        print(line)
        for row in reader:
            print(row)


def csv_to_dict(path):
    list_with_data = []
    with open(path) as file:
        reader = csv.reader(file)
        header = next(reader)
        for line in reader:
            temp = {}
            n = 0
            for title in header:
                temp[title] = line[n]
                n += 1
            list_with_data.append(temp)
    return list_with_data


def format_to_xml(path):
    input_data = csv_to_dict(path)
    root = ElementTree.Element("Users")
    n = 0
    for item in input_data:
        record = ElementTree.SubElement(root, 'user', {"id": f"{n}"})
        n += 1
        for key, value in item.items():
            e = ElementTree.SubElement(record, key)
            e.text = str(value)
    return root


def write_xml(root, path):
    # pretty output
    xmlstr = minidom.parseString(ElementTree.tostring(root)).toprettyxml(indent="   ")
    with open(path, 'w') as f:
        f.write(xmlstr)


def format_to_json(path):
    temp = csv_to_dict(path)
    data = json.dumps(temp, indent="    ")
    return data


def write_json_to_file(csv, path_save):
    temp = csv_to_dict(csv)
    with open(path_save, 'w') as file:
        json.dump(temp, file, indent="    ")


if __name__ == '__main__':
    # write_to_file('data/output.csv')
    # add_to_file('data/output.csv')'
    # read_file('data/output.csv')
    # root = format_to_xml('data/output.csv')
    # print(ElementTree.dump(root))
    # write_xml(root, 'data/output.xml')
    data = format_to_json('data/output.csv')
    print(data)
    write_json_to_file('data/output.csv', 'data/output.json')

