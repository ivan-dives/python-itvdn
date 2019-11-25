# Задание 3
# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.
import doctest
# doctest.testmod()


def stair(stair_n):
    '''
    >>> stair(0)
    0
    >>> stair(1)
    1
    >>> stair(2)
    2
    >>> stair(3)
    3
    >>> stair(4)
    5
    '''
    if stair_n in range(-1, 2):
        return stair_n + 1
    else:
        return stair(stair_n-1) + stair(stair_n-2)


doctest.run_docstring_examples(stair, None, verbose=True)
n = int(input('Enter the number of stair you want to climb: '))
print('Result: ', stair(n-1))
