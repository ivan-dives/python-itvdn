#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.etree import ElementTree as ET

tree = ET.parse('data/output.xml')
root = tree.getroot()
employees = list(root)

for employee_data in employees:
    print('ID: ', (employee_data.attrib, employee_data.get('id')))
    print('{} {} {}'.format(
        employee_data.find('./Name').text,
        employee_data.find('./Surname').text,
        employee_data.find('./Age').text
    ))