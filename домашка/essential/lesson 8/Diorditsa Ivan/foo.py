import pickle

class Klass:
    pass

k = Klass()
print(pickle.dumps(k))

exit()

#import cvs

import pickle

d = {'login': 'ivan', 'password': 'password'}

s = pickle.dumps(d)
print(f'{type(s)=} {s=}')

myset = {10, 20, 30, 40}
s1 = pickle.dumps(myset)
print(f'{type(s1)=} {s1=}')

myset1 = pickle.loads(s1)
print(myset1)

print(pickle.dumps([10, 20, 30, 40]))

exit()

import json

d = {'car1': 10, 'car2': 15}

with open('cars.txt', 'w') as f:
    # запись в файл
    json.dump(d, f)

with open('cars.txt', 'r') as f:
    # читаем и десериализуем из файла
    d2 = json.load(f)

print(d2)

exit()

myset = {10, 20, 30}

import json

s = json.dumps(myset)
print(f'{type(s)=} {s=}')

exit()

d = {'login': 'ivan', 'password': 'password'}

import json

# сериализовать
j = json.dumps(d)
#print(f'{j=}')

with open('credentials.txt', 'w') as f:
    f.write(j)

with open('credentials.txt', 'r') as f:
    s = f.read()

print(f'{type(s)=} {s=}')
# десериализовать
d2 = json.loads(s)
print(f'{type(d2)=} {d2=}')


exit()

class Klass:
    def __init__(self):
        print("hello from __init__")

    def __enter__(self):
        #os.open()
        print("hello from __enter__")
        return self

    def __exit__(self, *args):
        #os.close()
        print("hello from __exit__", args)

with Klass() as k:
    print(type(k))
    print("inside with")
    #raise Exception("myexception")

exit()

with open('string.txt', 'r') as f:
    s = f.read()

print(s)

exit()

f = open('string.txt', 'r')
#print(type(f))
print(f'{f.tell()=}')
print(f.read())
print(f'{f.tell()=}')
#f.close()
f.seek(0)
print(f.read())
f.close()

exit()

f = open('string.txt', 'w')
f.write('строка')
f.close()

#import os

#os.system("ls")

exit()

s = '12345'

import os

#print(os.O_APPEND, os.O_CREAT)
#print(os.O_APPEND | os.O_CREAT)
#exit()

print(f'{os.getcwd()=}')
fd = os.open('string.txt', os.O_WRONLY | os.O_CREAT)
#print(f'{os.tell(fd)=}')
#print(os.lseek(fd, 0, os.SEEK_CUR))
os.lseek(fd, 200, os.SEEK_CUR)
print(f'{fd=}')
print(type(s), s)
e = s.encode('utf-8')
print(type(e), e)
d = b'mystring'
print(type(d), d)
os.write(fd, s.encode('utf-8'))
os.write(fd, b'somethingother')
os.close(fd)
