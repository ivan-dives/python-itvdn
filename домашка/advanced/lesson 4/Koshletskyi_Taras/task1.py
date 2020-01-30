# Создайте функцию, которая создает класс, на основе переданных ей названия, атрибутов и методов. Необходимо, чтобы все
# названия переданных атрибутов и методов были приведены к нижнему регистру до создания класса.


def get_name(self):
    return self.name


def get_surname(self):
    return self.surname


def init(self, name, surname):
    self.first_name = name
    self.last_name = surname


attrs = {
    'name': '',
    'surname': '',
    'get_name': get_name,
    'get_surname': get_surname,
    '__init__': init
}


def create_class(class_name, attr):
    new_attr = {}
    class_name = class_name.lower()
    for k,v in attr.items():
        new_attr[k.lower()] = v
    return type(class_name, (object,), new_attr)


Foo = create_class("Takoe", attrs)
boo = Foo("Taras", "KOsh")
print(dir(Foo))
# boo.surname = "Kosh"
# boo.name = "Taras"

print(boo.get_name(), boo.get_surname())

