"""Модуль чтения данных и подведения итогов"""

import config
import pickle


# Функция чтения из файла чисел, предлставленных в виде строки,
# возвращающая сумму прочитанных чисел
def count_sum(filename):
    sm = 0
    with open(filename, 'rb') as file:
        try:
            while True:
                sm += pickle.load(file)
        except EOFError:
            pass
    return sm


if __name__ == '__main__':
    sum_ = count_sum(config.FILENAME)
    print('Sum =', sum_)
