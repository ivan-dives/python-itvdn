"""Модуль генерации и записи чисел"""

import random
import config


# Генератор случайных чисел
def generate_data():
    for i in range(config.COUNT):
        yield random.random()


# Функция записи в файл данных из итерабельного объекта
def write_data(dt_gen, filename):
    with open(filename, 'w') as file:
        for number in dt_gen:
            print(number, file=file)


if __name__ == '__main__':
    dt = generate_data()
    write_data(dt, config.FILENAME)
