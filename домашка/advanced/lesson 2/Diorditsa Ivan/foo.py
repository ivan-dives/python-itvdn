

xmltext = """
<library owner='ivan'>
    <book color='black'>
        <title>Программирование на Python</title>
    </book>
    <book color='write'>
        <title>Программирование на JavaScript</title>
    </book>
</library>
"""

exit()

import io
import csv

kvstr = \
"""
name=ivan
group=python
date=10.1
"""

s = io.StringIO(kvstr)
print(type(s))
reader = csv.reader(s, delimiter='=')
print('Line nums', reader.line_num)
print('Dialect', reader.dialect)
for row in reader:
    print(type(row), row)

exit()

import csv

with open('/home/ivan/Downloads/Python (Диордица) - Python (Диордица).csv', 'r') as f:
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)

exit()

csv = \
"""
one,two,three
ivan,ivan,roman
1,10,20
"""

exit()

import json

d = {'a': 10, 'b': 20}

s = json.dumps(d)
print(type(s), s)
