import doctest

#doctest.testmod()


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = fib(n-1)
        b = fib(n-2)
        c = a + b
        return c
        #return fib(n-1) + fib(n-2)


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

doctest.run_docstring_examples(stairs, globals(), verbose=True)

#n = input()
#n = int(n)
#s = stairs(n)
#print(s)
