# Задание
# Напишите функцию-генератор для получения n первых простых чисел.


def is_simple_num(n):
    """Функция проверяющая, является ли число простым"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def simple_gen(n):
    count = 1
    curr_val = 2

    if n < count:
        return None

    while count <= n:
        yield curr_val
        count += 1
        curr_val += 1
        while not is_simple_num(curr_val):
            curr_val += 1

    return


def main():
    while True:
        k = input("Введите требуемое количество простых чиcел (целое положительное число): ")
        try:
            k = int(k)
        except TypeError:
            continue
        if k < 1 :
            continue
        break

    for i in simple_gen(k):
        print(i, end="  ")


if __name__ == '__main__':
    main()
