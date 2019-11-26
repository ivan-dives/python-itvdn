# Задание 3
# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.
import doctest
# doctest.testmod()


def stair(stair_n):
    """
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
    """
    def stair_s(stair_num):
        if stair_num in range(0, 2):
            return stair_num
        else:
            return stair_s(stair_num-1) + stair_s(stair_num-2)

    if stair_n == 0:
        return 0
    else:
        return stair_s(stair_n+1)


doctest.run_docstring_examples(stair, None, verbose=True)
n = int(input('Enter the number of stair you want to climb: '))
print('Result: ', stair(n))
