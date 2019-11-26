def foo(y):
    '''Chisla Fibonachi'''
    if y == 1 or y == 0:
        return 1
    else:
        return foo(y-1)+foo(y-2)

print('Для выхода наберите "stop"')

while True:
    x = input('Введите количество ступенек на которое нужно подняться: ')
    if x == 'stop':
        print('Программа завершилась')
        break
    else:
        x = int(x)
        print(f'Количество методов = {foo(x)}')

