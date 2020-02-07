#import doctest

def calculator(s):
    """
    >>> calculator("2+2")
    4
    >>> calculator("2-3")
    -1
    >>> calculator("3/0")
    None
    """

    try:
        a, b = s.split("+")
        try:
            return int(a) + int(b)
        except ValueError:
            print(f"invalid numbers: {a=} {b=} (addition)")
    except ValueError:
        pass

    try:
        a, b = s.split("-")
        try:
            return int(a) - int(b)
        except ValueError:
            print(f"invalid numbers: {a=} {b=} (substraction)")
    except ValueError:
        pass


#print(calculator("0+bb"))
#exit()

#import doctest
#doctest.run_docstring_examples(calculator, None, verbose=True)

#print(calculator("10+10"))

#exit()

# assert
# doctests
# unittest
# pytest


#import unittest


def database_connected():
    return False

# ...
# ...

#assert database_connected() == True

# ...
# ...