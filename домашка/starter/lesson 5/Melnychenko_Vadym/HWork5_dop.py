def sredarf(x, y, z):
    sa = x + y + z
    sa = sa / 3
    return(sa)

while True:
    print('Для завершения работы программы напечатайте "STOP"', '\n')

    x = input('Введите первое число: ')
    if x.lower() == 'stop':
        print('Программа завершилась')
        break
    else:
        x = int(x)

    y = input('Введите второе число: ')
    if y.lower == 'stop':
        print('Программа завершилась')
        break
    else:
        y = int(y)

    o = input('Введите третье число: ')
    if o.lower == 'stop':
        print('Программа завершилась')
        break
    else:
        o = int(o)

    res = sredarf(x, y, o)
    print(f'среднее арифметическое = {res}', '\n')