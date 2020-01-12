def nprime(n):
    npool = []
    for x in range(2, n + 1):
        npool.append(x)
    i = 0
    while npool[i] ** 2 < n:
        for y in range(npool[i] ** 2, npool[-1] + 1, npool[i]):
            try:
                del npool[npool.index(y)]
            except ValueError:
                pass
        i += 1
    for z in npool:
        yield z
    return


for p in nprime(100):
    print(p)
