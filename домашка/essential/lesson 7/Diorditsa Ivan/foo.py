import sys as s

print(s.path)

exit()

from mymod import *

print(y)
#print(foo())

import sys
print(sys.modules['mymod'].foo())

exit()

import flask

exit()

def foo():
    return 2 + 2


if __name__ == '__main__':
    print(foo())

import mymod

print(f'inside foo: {__name__=}')

exit()

import pprint
import sys

sys.path.insert(0, '/путь/к/моей/папке/с/нечитаемым..!!!!!!90875328906)*?:;\именем')
pprint.pprint(sys.path)

exit()

import library.mylib

print(library.mylib.z)

#import library.mylib
#from ..library import y

#print(library.y)

#print(library.mylib.x)

exit()

import sys
import pprint

pprint.pprint(sys.path)

exit()

#print(sys.path)

try:
    import sys
except ImportError:
    import python2sys

import pprint

#print(type(__name__))

#print(type(sys))
#print(sys.__name__)

#pprint.pprint(dir(sys))
#print(dir(sys))

#pprint.pprint(sys.modules)

x = 20

#print(dir(sys.modules['__main__']))
#print(dir(sys.modules['sys']))

#print(sys.version)

#print(sys.modules['__main__'].x)
#print(sys.path)

#import mymod

#print(mymod.y)

#pprint.pprint(sys.modules)

#from mymod import y
from mymod import *

#pprint.pprint(sys.modules)
#print(mymod)
#print(sys.modules['mymod'])
#mymod.y
#print(sys.modules['mymod'].y)
#print(y)
print(foo())

def foo():
    return False

print(foo())
print(sys.modules['mymod'].foo())

myfoo = sys.modules['mymod'].foo
print(myfoo())

foo = 10

print(foo)


#print(mymod.foo())
#print(foo())
#print(sys.modules['mymod'].foo())

#print(mymod