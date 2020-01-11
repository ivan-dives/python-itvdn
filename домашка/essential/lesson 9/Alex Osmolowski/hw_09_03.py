# Задание 3
# Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в
# последовательности только чётные числа.


def even_numbers(generator):
    def decorated_sequence(*args):
        seq = generator(*args)
        return filter(lambda x: x % 2 == 0, seq)
    return decorated_sequence


@even_numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield b

def main():
    print(list(fibonacci(20)))


if __name__ == '__main__':
    main()
