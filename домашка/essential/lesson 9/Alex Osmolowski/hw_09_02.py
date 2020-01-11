# Задание 2
# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.


import random


def main():
    numbers = random.sample(range(100), 10)
    print('Оригинальный список:', numbers)

    odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
    print('Список нечётных чисел (функциональное программирование):', odd_numbers)
    odd_squares = map(lambda x: x ** 2, odd_numbers)
    print('Список квадратов нечётных чисел (функциональное программирование):', list(odd_squares))
    odd_squares_lc = [x ** 2 for x in numbers if x %2 == 1]
    print('Список квадратов нечётных чисел (list comprehension):', odd_squares_lc)


if __name__ == '__main__':
    main()
