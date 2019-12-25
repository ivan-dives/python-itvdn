lst = [-2, 0, 1, 4, 17, 5, -8, 64, 9, 72, -3]
print(lst)
odd = filter(lambda x: x % 2 == 1, lst)
res = map(lambda x: x ** 2, odd)
print(list(res))