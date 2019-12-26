def multi(x, y=5):
    return x * y


def multi_c(x):
    def second(y):
        return x * y
    return second


print(multi(10))
num = multi_c(15)
print(num(20))
