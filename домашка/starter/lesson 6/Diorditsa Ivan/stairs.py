import doctest

#doctest.testmod()

def __stairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return __stairs(n-1) + __stairs(n-2)

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
        return __stairs(n+1)

doctest.run_docstring_examples(stairs, globals(), verbose=True)

#n = input()
#n = int(n)
#s = stairs(n)
#print(s)

