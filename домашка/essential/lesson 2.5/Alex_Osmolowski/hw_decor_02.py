#  сделать декоратор, который печатает (print)
#  входные аргументы в функцию и то что функция возвращает.
#  Использовать его на своей последней домашке по ООП


class FuncPrint:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print("Функция: {}".format(self.func.__name__))
        print("Переданные параметры: {}".format(args))
        print("Полученный результат: {}".format(self.func(*args)))


@FuncPrint
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


@FuncPrint
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
        fib(n)
        print()
        fact(n)


if __name__ == '__main__':
    main()