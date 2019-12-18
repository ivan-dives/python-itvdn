import collections

def foo(*args, **kwargs):
    print(args, kwargs)

foo(1, 2, x=10, y=20)
#foo(x=10, y=20, 1, 2)

exit()

def foo(**kwargs):
    print(kwargs)

kwargs = { 'x' : 10, 'y' : 20}

foo(a=10, b=20, c=30)

def bar(x, y):
    print(x, y)

bar(**kwargs)

def foo(*args):
    print(args)

lst = [10, 20, 3]

foo(*lst)

exit()

print({1, 2, 3} == frozenset([1, 2, 3]))
print(set('abc') == frozenset('abc'))
print(set('abc') in set([frozenset('abc')]))

exit()

def get_ints(n):
    for i in range(n):
        yield i
        yield i + 1

print(list(get_ints(10)))  # все числа, возвращаемые генератором
print(set(get_ints(10)))   # множество содержит лишь уникальные значения

exit()

'''
class Klass:
    x = 10
    y = 20

print(Klass.__dict__)

exit()
'''

cars = {'пушкинская': 20, 'достоевского': 30}
print(cars)
print(cars['пушкинская'])
cars['героев днепра'] = '10 машин'
print(cars)
x = cars.get('грибоедовская', 'по умолчанию 100 машин')
print(x)

for key, value in cars.items():
    print(key, value)

print('hi')

for key in cars:
    print(key)

print(cars.keys())
print(cars.values())

exit()

l1 = (10, 20, [30, 40], 50)
print(l1)

#s = {100, 200, l1, 300}
#print(s)

print(hash((10, 20)))
print(hash((20, 30)))
print(hash((20, 30)))

exit()

s = frozenset(['Ivan', 'Vitaliy'])

print(s)
#s.add(20)

room1 = {'Ivan', "Vitaliy", 'Pavel'}
room2 = {'Alena', 'Oleksandr', 'Pavel'}

print(room1 & room2)
print(room1 | room2)
print(room2.issubset(room1))

exit()

myset = set()
myset.add(10)
myset.add(20)
myset.add(10)
myset.add(10)
myset.add(5)
myset.add('oxana')
myset.add(1.013)
#myset.add([10,20])
#myset.add(k)

print(myset)

exit()

class Klass:
    def __hash__(self):
        return hash("Ivan")

s = "Ivan"
print(hash(s))
print(hash("Ivan") % 3)
k = Klass()
print(hash(k))
print('tuple', hash((1,2,3)))
d = collections.deque()
print(hash(d))

print(hash(200))
print(hash(3.14))

#print(str.__hash__("foo"))
#print(hash("foo"))
#print(hash(500))

exit()

nt = collections.namedtuple('Point', ['x', 'y'])
o = nt(10, 20)

print(o[0])
print(o.x)

exit()

d = collections.deque()

d.append(10)
d.append(20)

print(d)

l = []

l.append(10)
l.append(20)

print(l)
