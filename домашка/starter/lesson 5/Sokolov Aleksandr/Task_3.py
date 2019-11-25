def oper_plus(a, b):
    return a + b

def oper_minus(a, b):
    return a - b

def oper_multiplication(a, b):
    return a * b

def oper_divizion(a, b):
    return a / b

while True:
    op = input('Enter operation sign(+,-,*,/): ')
    if op == 'exit':
        break
    if op in ('+', '-', '*', '/'):
        x = float(input('Enter 1-st number x = '))
        y = float(input('Enter 2-nd number y = '))
    if op == '+':
        print('Summ =  %.2f' % oper_plus(x, y))
    elif op == '-':
        print('Разность =  %.2f' % oper_minus(x, y))
    elif op == '*':
        print('Multiplication =  %.2f' % oper_multiplication(x, y))
    elif op == '/':
        if y != 0:
            print('Division =  %.2f' % oper_divizion(x, y))
        else:
            print('Division by zero!')
    else:
        print('You entered an invalid operation sign!')