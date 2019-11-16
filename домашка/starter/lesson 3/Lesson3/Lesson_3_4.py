print('Enter a, b, c for [ax^2 + bx + c = 0]')
a = int(input('Enter a first number (a): '))
b = int(input('Enter a second number (b): '))
c = int(input('Enter a thirst number (c): '))
d = b**2 - 4*a*c
print(f'D = {b}^2 - 4*{a}*{c} = {d}')

if d < 0:
    print('D < 0, then have no solution')
elif d == 0:
    d1 = -b/2*a
    print(f'D = 0, then solution is {d1}')
else:
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/2*a
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/2*a
    print('The first solution is x1={:4.2f}'.format(x1))
    print('The second solution is x2={:4.2f}'.format(x2))