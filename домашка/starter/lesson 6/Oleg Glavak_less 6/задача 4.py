
def tu(y):
    if a == y:
        return y
    elif y < a:
        return "eror"
    else:
        return y + tu(y - 1)


a = 10
y = 20
print(tu(y))


