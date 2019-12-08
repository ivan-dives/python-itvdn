from datetime import datetime

def how_long(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        print(f' от {args} будет {result}')
        return result
    return wrapper

@how_long
def fib( n ):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

@how_long
def fac( n ):
    if n == 0:
        return 1
    return fac(n - 1) * n
x = 5
print(fac(x))
print(fib(x))
_________________________________________________________________________________
вариант для одного
from datetime import datetime

def how_long(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        delta_time = datetime.now() - start
        global k
        k = f' от {args} будет {result}'
        return result

    return wrapper

@how_long
def fib( n ):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


x = 5
print(fib(x))
print(k)
______________________________________________________________________________________________________
from datetime import datetime

def how_long(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        delta_time = datetime.now() - start
        global k
        k = f' от {args} будет {result}'
        return result
    return wrapper



@how_long
def fac( n ):
    if n == 0:
        return 1
    return fac(n - 1) * n
x = 5
print(fac(x))
print(k)