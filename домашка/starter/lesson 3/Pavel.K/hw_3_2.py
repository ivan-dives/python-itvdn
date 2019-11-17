from math import pi as p, cos
x = float(input('put x in radians'))
if  -p <= x and x <= p:
    print(cos(3*x))
else:
    print(x)
