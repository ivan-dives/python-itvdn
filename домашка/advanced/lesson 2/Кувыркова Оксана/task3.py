import csv


class OneDialect(csv.Dialect):
    quoting = csv.QUOTE_MINIMAL
    quotechar = ";"
    delimiter = "~"
    lineterminator = '\n'


csv.register_dialect('new', OneDialect)


with open('csv_sample2.csv', 'w') as f:

    writer = csv.writer(f, dialect='new')

    writer.writerow(['item1', 'item2', 'item3'])
    writer.writerow(['one', 'two', 'three'])


with open('csv_sample2.csv', 'r') as f:
    reader = csv.DictReader(f, dialect='new')

    for row in reader:
        print(row)



class TwoDialect(csv.Dialect):
    quoting = csv.QUOTE_NONNUMERIC
    quotechar = "+"
    delimiter = "="
    lineterminator = '\n'


csv.register_dialect('second', TwoDialect)

with open('csv_sample2.csv', 'w') as f:

    writer = csv.writer(f, dialect='second')

    writer.writerow(['item1', 'item2', 'item3'])
    writer.writerow(['one', 'two', 'three'])


with open('csv_sample2.csv', 'r') as f:
    reader = csv.DictReader(f, dialect='second')
    # reader = csv.reader(f, dialect='second')

    for row in reader:
        print(row)