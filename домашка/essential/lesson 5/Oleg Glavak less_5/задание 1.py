def mid_ar(*x):
    return sum(x) / len(x)

l = [5, 3]

print(mid_ar(*l))
print(mid_ar(*range(2, 6)))