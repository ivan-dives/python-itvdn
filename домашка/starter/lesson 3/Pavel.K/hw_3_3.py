a, b, c = map(int, input('put a,b,c').split())
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f'{x1} {x2}')
elif discriminant == 0:
    print(-b / (2 * a))
else:
    print('only imaginary roots, no real')