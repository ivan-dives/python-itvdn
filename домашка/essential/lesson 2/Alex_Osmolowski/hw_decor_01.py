# сделать декоратор, который считает как долго функция работала
# и печатает результат (в миллисекундах или секундах) - посчитать
# с его помощью время работы функций фибоначчи и факториал


import time


def timer_count(f):
    def tm(n):
        start = time.time()
        res = f(n)
        fin = time.time()
        print("Время выполнения функции: {} ms".format((fin-start)*1000))
        return res
    return tm


@timer_count
def fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_lst = [1, 1]
        for i in range(n-2):
            fib_lst.append(fib_lst[i]+fib_lst[i+1])
        return fib_lst

@timer_count
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        fct = 1
        for i in range(1, n+1):
            fct *= i
        return fct


def main():
    n = input("Введите целое положительное число n = ")
    if not n.isdigit():
        print("Введено некорректное значение!")
    else:
        n = int(n)
        print("Последовательность Фибоначи из {} чисел = {}".format(n, fib(n)))
        print("{}! = {}".format(n, fact(n)))


if __name__ == '__main__':
    main()