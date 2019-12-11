x = input('Введите число Х от 0 до 5 с условем X<Y: ')
x = int(x)
y = input('Введите число Y от -5 до 0 с условем X<Y: ')
y = int(y)

def foo(arg1 ,arg2):
    if arg1 == arg2:
        print('Введены одинаковые числа')
    elif arg1 > arg2:
        print('Первое число больше второго')
    else:
        while arg1 < arg2:
            arg1 += 0.5
            print(arg1)

z = foo(x, y)
