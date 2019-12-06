import time

def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

def testtime(f):
    def dec(*a, **k):
        start_time = time.time()
        result = f(*a, **k)
        end_time = time.time()
        print("- Finished '{}', time = {:0.5f}s ".format(f.__name__,end_time - start_time))
        return result
    dec.__name__ = f.__name__
    return dec

@memoize
@testtime
def fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@memoize
@testtime
def fakt(n):
    if n == 0:
        return 1
    else:
        return fakt(n - 1) * n

n = 12

print(fibonacci(n))
print()
print(fakt(n))