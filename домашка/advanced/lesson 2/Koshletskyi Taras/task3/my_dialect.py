#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "`"
    doublequote = True
    delimiter = ";"
    lineterminator = '\r\n'


csv.register_dialect('taras_dialect', CustomDialect)

with open('data/output.csv', 'w') as f:
    # два варианта передачи диалекта
    # 2. передача класса диалекта
    # writer = csv.writer(f, dialect=CustomDialect)
    # 2. передача имени диалекта, который ма заранее зарегистрировали с этим
    # же именем.
    writer = csv.writer(f, dialect='taras_dialect')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])