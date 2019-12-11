def foo(a):
    return (12*a + 21) * (a + 8)
def bar(b):
    return (5*b - 14) * (b**2 - 23*b)
x = -5
while x <= 5:
    y = foo(x)
    z = bar(y)
    print(x, y, z, sep='__________')
    x += 0.5
