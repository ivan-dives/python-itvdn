class ErrorRange(Exception):
    pass

def fooerrorrange(x):
    if x < 20 or x > 400:
        raise ErrorRange('error')
    return x

while True:
    a = int(input('Введите значение от 20 до 400: '))
    try:
        fooerrorrange(a)
        print('Успех!')
        break
    except ErrorRange:
        print('Вы ввели число вне заданого диапазона\nпопробуйте еще раз')
        print()