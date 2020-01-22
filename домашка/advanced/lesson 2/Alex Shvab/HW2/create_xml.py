from xml.etree import ElementTree as ET


data = [
    {'title': "Everyday Italian", 'author': "Giada De Laurentiis", "year": 2005, "price": 30.00},
    {'title': "Harry Potter", 'author': "J K. Rowling", "year": 2005, "price": 29.99},
    {'title': "Learning XML", 'author': "Erik T. Ray", "year": 2003, "price": 39.95},
    {'title': "The Divine Comedy", 'author': "Dante Alighieri", "year": 1348, "price": 42.50},
    {'title': "The Gentle Grafter", 'author': "O. Henry", "year": 1908, "price": 10.15},
]

root = ET.Element("bookstore")

for item in data:
    book = ET.SubElement(root, "book")
    for key, value in item.items():
        e = ET.SubElement(book, key)
        e.text = str(value)


tree = ET.ElementTree(root)
tree.write("bookshop.xml", encoding="utf-8")