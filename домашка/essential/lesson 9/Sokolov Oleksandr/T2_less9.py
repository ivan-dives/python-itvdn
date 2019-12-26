
c = filter(lambda a: a % 2 == 1, [2, 7, 5, 4, 10, 9])
b = map(lambda a: a ** 2, c)
print(list(b))