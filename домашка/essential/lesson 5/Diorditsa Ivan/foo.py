
l1 = [20]
l2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]

print(l1 > l2)
print(len(l1) > len(l2))

s1 = 'z'
s2 = 'aaaaaaaaaaaaaaa'

print(s1 > s2)

exit()

# Список кортежей
tuples = [(x, y) for x in range(3) for y in range(3)]
# Итерирование списка
for t in tuples:
    print(t)
# Итерирование с распаковкой
for x, y in tuples:
    print(x, y)

exit()

def foo(x=None, *args):
    print(id(args), args)
    #return sum(args)

foo()


#def foo(*tup):
#    #print(type(tup), tup)
#
#    return sum(tup)

print(foo(1, 2, 3, 10, 15))

exit()

def foo(a, b, c, d):
    print(a, b, c, d)

lst = [2, 3, 4, 5]

a, b, c, d = lst

foo(*lst)

exit()

def foo(x, y):
    return x + y

print(foo(2, 3))

exit()

lst1 = [1, 2, [3]]
print(id(lst1), lst1, id(lst1[2]))

tup = tuple(lst1)
print(id(tup), tup, id(tup[2]))

lst2 = list(tup)
print(id(lst2), lst2, id(lst2[2]))

exit()

class Mutable:
    def __init__(self):
        self.x = 10

class Immutable:
    def __init__(self):
        self.x = 10
    def __setattr__(self, key, value):
        raise Exception("Not mutable")

mut = Mutable()
mut.x = 20

imm = Immutable()
imm.x = 20

exit()

lst = [1, 2, 3]
tup = (1, 2, 3)

print(id(lst), lst)
lst += [20,]
print(id(lst), lst)

print(id(tup), tup)
tup += (20,)
print(id(tup), tup)

x = 20,

print(type(x))

exit()

lst1 = [1, [2]]
#lst2 = lst1

#print(id(lst1), id(lst2))

#lst2 = lst1.copy()
#print(id(lst1), id(lst2))
#print(id(lst1[1]), id(lst2[1]))
#lst1[1].append(20)
#print(lst2[1])

import copy

#lst2 = copy.deepcopy(lst1)
#print(id(lst1), id(lst2))
#print(id(lst1[0]), id(lst2[0]))
#print(id(lst1[1]), id(lst2[1]))

lst2 = lst1[:]
print(id(lst1), id(lst2))
print(id(lst1[0]), id(lst2[0]))
print(id(lst1[1]), id(lst2[1]))


exit()

class Klass:
    def __delitem__(self, key):
        print(key)

    def __del__(self):
        print('I am in destructor')

k = Klass()
del k[10:100]

del k

exit()

lst = [ 1, 2, 3, 4, 5 ]

m = max(lst)
print(m)
i = lst.index(m)
print(i)

exit()

s = '12345'

print(s.index('5'))

#class Klass:

#s = 'abcd'

#print(s.index('c'))

exit()

class Klass:
    def __getitem__(self, item):
        print(type(item), item) # dir(item)
        if isinstance(item, slice):
            print(f'{item.start=}, {item.stop=}, {item.step=}')

k = Klass()
print(k[1:2:3])
print(k[10])

exit()

lst = [1, 2]
print(id(lst), lst)

lst *= 10
print(id(lst), lst)

lst[3] = 10
print(id(lst), lst)

s = 'ура '
print(id(s), s)

s *= 5
print(id(s), s)


exit()

print([1, 2] + [3,4])
print([5, 6] + ['строка'])

exit()

class Klass:
    def __contains__(self, item):
        if item == 'доска':
            return True

k = Klass()
print('мышь' not in k)

exit()

r = range(100, 120)

c = 0
for i in range(20):
    print(f'{c=} {i=}')
    c += 1

exit()

class C:
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration

c = C()

print('s' in c)