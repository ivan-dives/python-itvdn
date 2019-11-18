import math

x = float(input('число X: '))
oper = input('операция: ')
res = None

if oper == '+':
    y = float(input('число Y: '))
    res = x + y
elif oper == '-':
    y = float(input('число Y: '))
    res = x - y
elif oper == '*':
    y = float(input('число Y: '))
    res = x * y
elif oper == '/':
    y = float(input('число Y: '))
    res = x / y
elif oper == '^':
    y = float(input('число Y: '))
    res = x ** y
elif oper == 'sin':
    res = math.sin(x)
elif oper == 'cos':
    res = math.cos(x)
elif oper == 'tan':
    res = math.tan(x)
else:
    print('Неподдерживаемая операция')
if res is not None:
    print('Результат = ', res)