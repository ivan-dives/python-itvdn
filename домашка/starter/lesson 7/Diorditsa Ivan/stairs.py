#import doctest

MEMOIZE = [0, 1]


# def _fib(n):
#     try:
#         return MEMOIZE[n]
#     except:
#         v = fib(n-1) + fib(n-2)
#         MEMOIZE.insert(n, v)
#         return v


def fib(n):
    if len(MEMOIZE) > n:
        return MEMOIZE[n]
    else:
        v = fib(n-1) + fib(n-2)
        MEMOIZE.insert(n, v)
        return v


def stairs(n):
    '''
    >>> stairs(0)
    0
    >>> stairs(1)
    1
    >>> stairs(2)
    2
    >>> stairs(3)
    3
    >>> stairs(4)
    5
    '''
    if n == 0:
        return 0
    else:
        return fib(n+1)

#doctest.run_docstring_examples(stairs, None, verbose=True)

print(stairs(200))

print(MEMOIZE)