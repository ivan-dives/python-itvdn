# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.
# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.


class ArgumentIsZero(BaseException):
    pass


def arg_is_zero(f, s, operation):
    if f == 0 or s == 0:
        ex = ArgumentIsZero('Error by zero argument.')
        raise ex
    if operation == '+':
        return f + s
    elif operation == '-':
        return f - s


while True:
    op = input('Enter operation (+, -, *, /, ^) or write (end) to interrupt calculation: ')
    if op in ['+', '-', '*', '/']:
        try:
            a = int(input('First number: '))
            b = int(input('Second number: '))
        except ValueError as ex_num:
            print('One or both numbers are not number.\n')
            continue
        if op == '+':
            try:
                print(f'Result {a} + {b} = {arg_is_zero(a, b, op)}\n')
            except ArgumentIsZero as ex_add:
                print('Argument is zero, why do you try to do this operation?\n')
        if op == '-':
            try:
                print(f'Result {a} - {b} = {arg_is_zero(a, b, op)}\n')
            except ArgumentIsZero as ex_sub:
                print('Argument is zero, why do you try to do this operation?\n')
        if op == '*':
            print(f'Result {a} * {b} = {a*b}\n')
        if op == '/':
            try:
                print(f'Result {a} / {b} = {a/b}\n')
            except ZeroDivisionError as zer0_div:
                print('Division by zero.\n')
    elif op == '^':
        try:
            c = int(input('Enter a number: '))
            d = int(input('Enter a power: '))
        except ValueError as ex_num:
            print('Number or power is not number.\n')
            continue
        try:
            print(f'Result of {c}^{d} = {c ** d}\n')
        except ZeroDivisionError as zer0_pow:
            print('Power of zero cannot be a negative number.\n')
    elif op == 'end':
        break
    else:
        print('You have entered wrong command, try again.\n')
