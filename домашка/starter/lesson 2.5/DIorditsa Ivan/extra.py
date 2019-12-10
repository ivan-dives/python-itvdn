# декорирование классом

import time


class Timer:
    def __init__(self, f):
        self.f = f
        self.counter = 0

    def __call__(self, n):
        if self.counter == 0:
            self.start_time = time.time()
        self.counter += 1
        print(f"IN {self.counter=}")
        r = self.f(n)
        self.counter -= 1
        print(f"OUT {self.counter=}")
        if self.counter == 0:
            print(time.time() - self.start_time)
        return r

@Timer
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n * recur_factorial(n-1)

print(type(recur_factorial))

#print(recur_factorial(10))

exit()

class Klass:
    @classmethod
    def run(self):
        print('я бегу')


#k = Klass()
#k.run()

Klass.run()

exit()

class Klass:
    __value = 30

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newval):
        self.__value = newval

k = Klass()
print(k.value)
k.value = 20
print(k.value)


exit()

def checker(f, a=0):
    if a != 0:
        return None

    def tmp(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            return None
        if x is None or y is None:
            return None
        if not callable(f):
             return None
        ret = f(x, y)
        if ret < 0:
            print('ret < 0')
        return ret

    return tmp


#div = checker(div, a=1)
@checker(a=1)
def div(x, y):
    return x / y

#add = checker(add)
@checker
def add(x, y):
    return x + y

@checker
def sub(x, y):
    return x - y

print(div(-10, 20))

exit()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def checker(f, x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    if x is None or y is None:
        return None
    if not callable(f):
        return None
    return f(x, y)

print(checker(add, 10, '20'))
print(checker(10, 10, 10))
print(checker(sub, 20, 30))

exit()

def add(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    if x is None or y is None:
        return None
    return x + y


def div(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    if x is None or y is None:
        return None
    return x / y


def sub(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    if x is None or y is None:
        return None
    return x - y

print(add(1, "2"))


exit()

class Mouse:
    def click(self, poly, x, y):
        poly.send_coordinates(x, y)


class Polygon:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


    def send_coordinates(self, x, y):
        if self.top <= x <= self.bottom and self.left <= y <= self.right:
            print("на нас кликнули")
        else:
            print('нас не кликнули')


p = Polygon(100, 200, 200, 300)
m = Mouse()

m.click(p, 0, 0)
m.click(p, 150, 250)
