def decor(fun):
    def new_fun(n):
        lst = fun(n)
        return filter(lambda x: x % 2 == 0, lst)
    return new_fun()


def fib(n):
    head = 0
    tail = 1
    for i in range(n):
        head = tail
        tail = head + tail
        yield tail

print(list(fib(10)))