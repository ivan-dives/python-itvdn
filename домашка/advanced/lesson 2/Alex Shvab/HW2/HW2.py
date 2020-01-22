from xml.etree import ElementTree as ET


tree = ET.parse("bookshop.xml")
root = tree.getroot()
#children = root.getchildren()

for book in root:
    print("category: ", (book.attrib, book.get("category")))
    print("{} {} {} {}".format(
        book.find("./title").text,
        book.find("./author").text,
        book.find("./year").text,
        book.find("./price").text
    ))
print()

title = root.findall("./book/title")
author = root.findall("./book/author")
year = root.findall("./book/year")
price = root.findall("./book/price")

for value in zip(title, author, year, price):
    row = {value.tag: value.text for value in value}
    print(row)
print()


title = root.findall("./book[@category='NOVEL']/title")
author = root.findall("./book[@category='NOVEL']/author")
year = root.findall("./book[@category='NOVEL']/year")
price = root.findall("./book[@category='NOVEL']/price")

for value in zip(title, author, year, price):
    row = {value.tag: value.text for value in value}
    print(row)
