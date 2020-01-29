def foo(name, bases, _dict):
    print(name, bases, _dict)
    name = name.lower()
    newdict = {}
    for k, v in _dict.items():
        newdict[k.lower()] = v
    print(name, bases, newdict)
    return type(f'{name}', bases, newdict)

def myinit(cls, hieght):
    cls.hieght = hieght

foo("LOL", (object,), dict(__INIT__= myinit, X = 20))