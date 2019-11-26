import doctest   
import functools
@functools.lru_cache(maxsize=None)


def fib(n):
  
    '''
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(3)
    3
    >>> fib(4)
    5
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

doctest.run_docstring_examples(fib, None, verbose=True) 
print(fib(int(input('put number Fibonacci'))))
