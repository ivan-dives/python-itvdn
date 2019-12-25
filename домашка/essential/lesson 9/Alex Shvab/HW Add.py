from functools import partial


def simp_mult(x, y):
    return x * y


res = partial(simp_mult, y=2)
print(res(10))


def car_mult(x):

    def mult(y):
        return x * y

    return mult

result = partial(car_mult, x = 2)
print(result()(6))

