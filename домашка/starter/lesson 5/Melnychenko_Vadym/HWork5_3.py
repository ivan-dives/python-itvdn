def plus(a, b):
    o = a + b
    return o

def minus(a, b):
    o = a - b
    return o

def umnogh(a, b):
    o = a * b
    return o

def deln(a, b):
    if b == 0:
        return "На ноль деление запрещено"
    else:
        o = a / b
        return o


while True:
    print('Для завершения работы программы напечатайте "STOP"', '\n')

    x = input('Введите первое число: ')
    if x.lower() == 'stop':
        print('Программа завершилась')
        break
    else:
        x = int(x)

    o = input('Введите операцию которою хотите выполнить (+, -, *, /): ')
    if o.lower == 'stop':
        print('Программа завершилась')
        break

    y = input('Введите второе число: ')
    if y.lower == 'stop':
        print('Программа завершилась')
        break
    else:
        y = int(y)


    if o == '+':
        r = plus(x, y)
        print(f'Результат: {r}' '\n')

    elif o == '-':
        r = minus(x, y)
        print(f'Результат: {r}' '\n')

    elif o == '*':
        r = umnogh(x, y)
        print(f'Результат: {r}' '\n')

    elif o == '/':
        r = deln(x, y)
        print(f'Результат: {r}' '\n')

    else:
        print('Не верная операция, повторите попытку', '\n')
