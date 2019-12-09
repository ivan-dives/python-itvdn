# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.


while True:
    op = input('Enter operation (+, -, *, /, ^) or write (end) to interrupt calculation: ')
    if op in ['+', '-', '*', '/']:
        a = int(input('First: '))
        b = int(input('Second: '))
        if op == '+':
            print(f'Result {a} + {b} = {a+b}')
        if op == '-':
            print(f'Result {a} - {b} = {a-b}')
        if op == '*':
            print(f'Result {a} * {b} = {a*b}')
        if op == '/':
            try:
                print(f'Result {a} / {b} = {a/b}')
            except ZeroDivisionError as zer0_div:
                print('Division by zero')
    elif op == '^':
        c = int(input('Enter a number: '))
        d = int(input('Enter a power: '))
        try:
            print(f'Result of {c}^{d} = {c ** d}')
        except ZeroDivisionError as zer0_pow:
            print('Power of zero cannot be a negative number')
    elif op == 'end':
        break
    else:
        print('You have entered wrong command, try again.')
