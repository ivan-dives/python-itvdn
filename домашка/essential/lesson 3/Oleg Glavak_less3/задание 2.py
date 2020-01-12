from operator import add, sub, mul, truediv, pow

oper = {'+': add, '-': sub, '*': mul, '/': truediv, '^': pow }

try:
    x = float(input("Enter value 1: "))
    z = input("Enter symbol: ")
    y = float(input("Enter value 2: "))
    result = oper[z] (x, y)
except ValueError:
    print('Incorrect input')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('=', result)