# Задание
# Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
# Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу.

from functools import partial

def ordinary_mult(x, y):
    """Обычная функция"""
    return x * y

def curryied_mult(x):
    """Каррированная функция"""

    def do_mult(y):
        return x * y

    return do_mult


def main():
    mult_to_10_ord = partial(ordinary_mult, 10)
    mult_to_10_curr = curryied_mult(10)

    print('Обычная функция 10 * 25:', mult_to_10_ord(25))
    print('Каррированная функция 10 * 25:', mult_to_10_curr(25))


if __name__ == '__main__':
    main()