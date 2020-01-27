#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

path = 'data/output.csv'


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "`"
    doublequote = True
    delimiter = ";"
    lineterminator = '\r\n'


def make_file(path_output):
    csv.register_dialect('taras_dialect', CustomDialect)
    with open(path_output, 'w') as f:
        writer = csv.writer(f, dialect='taras_dialect')
        for i in range(5):
            writer.writerow(['1', '2', '3'])
            print()


def parse_csv(path_input):
    csv.register_dialect('taras_dialect', CustomDialect)
    with open(path_input, 'r') as f:
        reader = csv.reader(f, dialect='taras_dialect')
        # print('Dialect: --->', reader.dialect)
        for row in reader:
            print(row)


if __name__ == '__main__':
    make_file(path)
    parse_csv(path)
