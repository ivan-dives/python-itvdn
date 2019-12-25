def foo():
    x = 10

    def f(x=x):
        print(x)

    x = 50

    return f

x = foo()
x()

exit()

import functools

def foo(a, b):
    return a + b

foo1 = functools.partial(foo, 10)

print(foo1(30))

exit()

def foo(x, y):
    return x + y


bar = lambda a, b=10: a+b

print(bar(40,50))

l = [1, 2, 3, 4, 5]


def f(y):
    return y * y

print(list(map(f, l)))
print(list(map(lambda y: y*y, l)))
print([y*y for y in l])


print(list(filter(lambda x: x<3, l)))
print([x for x in l if x < 3])

import functools
print(functools.reduce(lambda a,b:a+b, l))

exit()

x = 100


def decor(f):
    x = 10

    def new_foo(y):
        print('I am in new_foo now')
        return f(x, y)
    return new_foo


@decor
def foo(x, y):
    return x + y


print(foo(20))
print(foo.__closure__[1].cell_contents)

exit()

def foo(x, y):
    return x + y


def bar(f):
    print(f(2, 3))
    print(f.z)


foo.z = 30
bar(foo)

exit()

d = {'name': 'ivan', 'password': 'password'}

import pickle

s = pickle.dumps(d)

import base64

d2 = {'temp': base64.b64encode(s).decode('utf-8')}

print(d2)

import json

s2 = json.dumps(d2)

print(s2)