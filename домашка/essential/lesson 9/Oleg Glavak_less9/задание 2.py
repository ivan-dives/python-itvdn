l = [7, 12, 4, 9, 31, 47, 52]
r = list(filter(lambda x : x % 2, l))
sq = list(map(lambda x : x ** 2, r))
print(sq)