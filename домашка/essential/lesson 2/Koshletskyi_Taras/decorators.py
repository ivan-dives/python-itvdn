import time
from datetime import datetime


def clock(func):

    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


def measure_time(func):

    def tmp(n):
        start = time.time()
        res = func(n)
        end = time.time()
        diff = round(end - start, 4)
        print(diff)
        return res

    return tmp


def how_long(func):
    def wrapper(*args, **kwargs):

        start = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        return delta_time

    return wrapper


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


@clock
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


@measure_time
def foo(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def main():
    print(fibonacci(30))
    print(fibonacci(10))
    print(fac(10))
    print(foo(10))

if __name__ == '__main__':
    main()