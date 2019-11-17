import math

x = input(f'Введите значение Х: ')
x = float(x)
pi = round(math.pi, 2)

if -pi <= x and x <= pi:
    y = math.cos(3*x)
    print(f'y = {round(y, 2)}')
else:
    #x < -pi and x > pi
    print(f'y = {x}')
