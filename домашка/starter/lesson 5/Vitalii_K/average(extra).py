def foo(a, b, c):
    return (a + b + c) / 3
while True:
    x = int(input('First number: '))
    y = int(input('Second number: '))
    z = int(input('Third number: '))
    print(f'The avarage of ({x}, {y}, {z}) is: {round(foo(x, y, z))}')
