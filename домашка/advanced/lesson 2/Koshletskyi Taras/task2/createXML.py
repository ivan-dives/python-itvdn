#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from xml.dom import minidom

data = [
    {"Name": "Andrey", "Surname": "Petrov", "Age": "40", "Male": "M"},
    {"Name": "Ivan", "Surname": "Petrov", "Age": "12", "Male": "M"},
    {"Name": "Paul", "Surname": "Ivanov", "Age": "35", "Male": "M"},
    {"Name": "Anatolii", "Surname": "Suleyman", "Age": "25", "Male": "M"},
    {"Name": "Petro", "Surname": "Tako", "Age": "20", "Male": "M"},
    {"Name": "Masha", "Surname": "Bonia", "Age": "22", "Male": "F"}
]
xml_write_path = 'data/output.xml'


def create_simple_xml(input_data):
    root = ElementTree.Element("Manufacture")
    n = 0
    for item in input_data:
        record = ElementTree.SubElement(root, 'employee', {"id": f"{n}"})
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
    # tree = ElementTree.ElementTree(root)
    # tree.write('data/output.xml', encoding='utf-8')


def main():
    root = create_simple_xml(data)
    write_xml(root, xml_write_path)


if __name__ == '__main__':
    main()

