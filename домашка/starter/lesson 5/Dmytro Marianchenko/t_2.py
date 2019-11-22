print()
def neg(b,a=10):
    while b < 0:
        b += 0.5
        s=b*a
        print(f"a = {a}, b = {b}, total = {s}")


def pos(b,a=10):
    while b < 5:
        b += 0.5
        s = b * a
        print(f"a = {a}, b = {b}, total = {s}")

neg(-5)
pos(0)