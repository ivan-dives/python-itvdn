"""Модуль чтения данных и подведения итогов"""

import config

# Функция чтения из файла чисел, предлставленных в виде строки,
# возвращающая сумму прочитанных чисел
def count_sum(filename):
    sm = 0
    with open(filename, 'r') as file:
        for line in file:
            try:
                numb = float(line)
            except ValueError:
                pass
            else:
                sm += numb
    return sm


if __name__ == '__main__':
    sum_ = count_sum(config.FILENAME)
    print('Sum =', sum_)
