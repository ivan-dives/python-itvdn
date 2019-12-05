import math

x = float(input("Введите значение x: "))

if x >= - math.pi or x <= math.pi:
    y = math.cos(x*3)
else:
    y = x
print(y)