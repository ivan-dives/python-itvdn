def revv(l):
    k = []
    for x in l:
        k.insert(0, x)
    l = k
    return l

c = [7, 20, 45, 57, 60]

print(revv(c))