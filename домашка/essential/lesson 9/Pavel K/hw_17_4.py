# Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
# Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу.

import functools
def first_mult(x,y):
    return x*y

result = functools.partial(first_mult, y = 10)
print(result(20)) # 200

#################################################################
def second_mult(x):

    def mult(y):
        return x * y
    return mult

resultforsecond_m = functools.partial(second_mult, x= 4)
print(resultforsecond_m()(12)) #48
