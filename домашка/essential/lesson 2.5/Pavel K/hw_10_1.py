from datetime import datetime

def how_long(func):
    def wrapper(*args, **kwargs):

        start = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        return delta_time
    return wrapper


@how_long
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

@how_long
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(15))#(int(input('_'))))
print(fib(15))#(int(input('_'))))