import math

x = input("Введите значение Х: ")
x = float(x)

if - math.pi <= x <= math.pi:
    y = math.cos(3*x)
    print("y = Cos(3x) = {}".format(y))
else:
    y = x
    print("y = x = {}".format(y))