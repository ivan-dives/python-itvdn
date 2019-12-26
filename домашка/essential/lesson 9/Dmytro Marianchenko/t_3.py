def decor(fun):
    def wrapper(*args):
        result = fun(*args)
        lst = list(filter(lambda x: x % 2 == 0, result))
        return lst

    return wrapper


@decor
def fib(var):
    x, y = 0, 1
    for i in range(var):
        x, y = y, x + y
        yield x


print(fib(15))
