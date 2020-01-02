from functools import partial

def mult(x, y):
    return x * y

mul = partial(mult, 7)
print(mul(3))
print(mul(10))

###############################################

def curryied_mult(x):
    def to_mult(y):
        return x * y
    return to_mult

mult= curryied_mult(6)
print(mult(5))