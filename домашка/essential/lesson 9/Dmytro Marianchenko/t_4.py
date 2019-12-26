def multi(x, y=5):
    return x * y


def multi_c(x):
    def second(y=25):
        return x * y
    return second


print(multi(10))
print(multi_c(20)())
