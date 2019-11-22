def square_root(a):
    return a ** 0.5


def expreccion_2(a):
    return 2 * a + a **2

for a in range(-5, 5, 1):
    print('square root =', (square_root(a)/2))
    print('2a + a^2 = ', (expreccion_2(a)/2))


