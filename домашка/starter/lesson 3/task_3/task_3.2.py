import math

x = float(input('x = '))
y = None

if -math.pi <= x <= math.pi:
    y = math.cos(3*x)

else:
    x < -math.pi or x > math.pi
    y = x

print(y)