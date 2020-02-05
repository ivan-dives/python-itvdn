# Створити функцію num_stat(n) яка на вхід отримує ціле невід'ємне число
# і поверетає кортеж (tuple) із наступними даними:
#
# кількість цифр даного число,
# суму цифр даного числа,
# добуток цифр даного числа


def num_stat(n):
    sn = str(n)
    ln = len(sn)
    sum = 0
    mlt = 1
    for s in sn:
        i = int(s)
        sum += i
        mlt *= i
    return ln, sum, mlt


print(num_stat(24))