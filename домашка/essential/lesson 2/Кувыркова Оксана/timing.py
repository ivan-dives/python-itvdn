from datetime import datetime
from functools import wraps
def timecount(func):
    @wraps(func)
    def wrap(*args, **kw):
        start = datetime.now()
        func(*args, **kw)
        finish = datetime.now()
        print(f"Time for executing {func.__name__} is {(finish - start)*1000} second")
    return wrap


@timecount
def factorial(x=10):
    f = 1
    while x > 1:
        f *= x
        x -= 1
    return f
    print (f"factorial from {x} is {f}")

@timecount
def fibonacci(y):
    fib1 = fib2 = 1
    n = y - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    print(fib2)


factorial(65434)
fibonacci(30000)