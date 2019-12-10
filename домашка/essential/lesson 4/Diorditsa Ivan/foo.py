class C:
    s = 'abcd'

    def __getitem__(self, index):
        print(f'requested {index=}')
        #return self.s[index]

c = C()
print(c[1::3])

exit()

s = 'abcd'

for i, c in enumerate(s):
    print(i, c)

exit()

def bar():
    return 10

def baz():
    yield 10

print('__iter__' in dir(bar))
b = baz()
b.close()
print(next(b))
#print('__iter__' in dir(b))
#print(dir(b))

exit()

# корутина после того как вызовем

def foo():
    i = 0
    while i < 3:
        i = yield i
        print(f'received {x=}')
        i += 1

f = foo()
print(next(f))
f.send(20)
f.send(30)

exit()

s = 'abc'

def foo():
    i = 0
    while i < 3:
        print('before')
        yield from (c.upper() for c in s)
        print('after')
        i += 1

for x in foo():
    print(x)

exit()

s = 'abcd'

l = (c.upper() for c in s)
print(next(l))
print(next(l))

exit()

#gen = (yield x for x in range(10))



#x = iter(range(10))
#print(next(x))

print(list(range(5)))

exit()

def bar(i):
    print('function begin')
    l = [1, 2, 3, 4]

    while True:
        try:
            item = l[i]
        except IndexError:
            return

        i += 1
        print(f'before yield {i=}')
        yield item
        print(f'after yield {i=}')

#for i in bar():
#    print(i)

print(bar(2))

b = bar(2)
c = bar(1)
d = bar(3)

#print(next(b))
#print(type(b))
#print(next(b))
#print(next(b))

exit()

#def foo():
#    l = [1, 2, 3, 4]
#
#    return l

print (foo())

exit()

'''
class Pointer:
    def __init__(self, o):
        self.o = o
        self.index = 0

    def __next__(self):
        while True:
            try:
                car = self.o.cars[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            if car.startswith('volvo'):
                return car
'''


class C:
    cars = ['volvo red', 'mazda red', 'volvo black', 'volvo blue']

    def __init__(self):
        self.index = 0

    def __iter__(self):
        #return Pointer(self)
        return self

    def __next__(self):
        while True:
            try:
                car = self.cars[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            if car.startswith('volvo'):
                return car

c = C()

#for x in c:
#    print(x)

try:
    i = iter(c)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration:
    pass














'''


class A:
    def __init__(self):
        self.i = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            self.i -= 1
            return self.i
        else:
            raise StopIteration

    def __getitem__(self, item):
        print(item) or raise IndexError

print(A()[20])

#for i in A():
#    print(i)

'''