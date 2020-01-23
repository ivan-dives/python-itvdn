import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = ":"
    delimiter = ";"
    lineterminator = "\n"


csv.register_dialect("mydialect", CustomDialect)


with open("mycsv.csv", "w") as  file:
    writer = csv.writer(file, dialect="mydialect")
    writer.writerow(["Everyday Italian","Giada De Laurentiis", 2005, 30.00])
    writer.writerow(["Harry Potter", "J K. Rowling", 2005, 29.99])
    writer.writerow(["Learning XML", "Erik T. Ray", 2003, 39.95])
    writer.writerow(["The Divine Comedy", "Dante Alighieri", 1348, 42.50])
    writer.writerow(["The Gentle Grafter", "O. Henry", 1908, 10.15])


sniffer = csv.Sniffer()
dialect = None


with open("mycsv.csv", "r") as file:
    content = file.read()
    dialect = sniffer.sniff(content)


print(dialect.delimiter, dialect.doublequote, dialect.quoting)


with open("mycsv.csv", "r") as file:
    reader = csv.reader(file, dialect=dialect)
    for row in reader:
        print(row)