CACHE = [0,1]


def stairs(n):
    if len(CACHE) > n:
        return CACHE[n]
    if n < 2:
        return 1
    res = stairs(n-1) + stairs(n-2)
    CACHE.append(res)
    return res


print(stairs(10))

