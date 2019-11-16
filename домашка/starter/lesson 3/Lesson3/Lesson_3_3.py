from math import pi, cos

x = int(input('Enter x for system of equations: '))
if -pi <= x <= pi:
    y = cos(3*x)
    print ('Solution of y = cos({}) is {:4.2f}'.format(3*x, y))
elif (x < -pi) or (x > pi):
    y = x
    print(f'Solution of y = x is {y}')