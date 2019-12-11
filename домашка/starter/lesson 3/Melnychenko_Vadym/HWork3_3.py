a = input('enter the number "a": ')
a = int(a)
b = input('enter the number "b": ')
b = int(b)
c = input('enter the number "c": ')
c = int(c)

D = (b**2)-4*a*c
if D > 0:
    x1 = (-b + (D**0.5))/(2*a)
    x2 = (-b - (D**0.5))/(2*a)
    print(f'D = {D}')
    print("x1 = " '%.2f' % x1)
    print("x2 = " '%.2f' % x2)
elif D == 0:
    x3 = (-b / (2*a))
    print(f'D = {D}')
    print("x = " '%.2f' % x3)
else:
    D = None
    print(f'D = {D}')