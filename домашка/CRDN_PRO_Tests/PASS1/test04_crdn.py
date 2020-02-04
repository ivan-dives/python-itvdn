# Створити функцію num_stat(n) яка на вхід отримує ціле невід'ємне число
# і поверетає кортеж (tuple) із наступними даними:
#
# кількість цифр даного число,
# суму цифр даного числа,
# добуток цифр даного числа

from functools import reduce

def num_split(n):
    if n == 0:
        return [0]

    res = []
    while n > 0:
        res.insert(0, n % 10)
        n = n // 10
    return res


def num_stat(n):
    num_digits = num_split(n)

    return (
        len(num_digits),
        sum(num_digits),
        reduce(lambda x, y: x * y, num_digits),
    )


print(num_stat(24))