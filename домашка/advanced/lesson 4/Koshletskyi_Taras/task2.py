# Создайте метакласс, который проверяет класс на запрет использования цифр в именах атрибутов и методах,
# а также верхнего регистра. Генерировать исключение, если данные правила нарушены

import string

checking = string.digits + string.ascii_uppercase


def check(name, bases, _dict):
    newdict = {}
    for k, v in _dict.items():
        for el in k:
            if el in checking:
                raise Exception("Not supported el")
    return type(name, bases, newdict)


class Foo(metaclass=check):

    name1 = "takoe"


boo = Foo()

print(boo)
