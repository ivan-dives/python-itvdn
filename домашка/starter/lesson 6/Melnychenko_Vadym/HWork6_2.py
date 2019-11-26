def foo(polindrom):
    z = polindrom
    if polindrom == z[::-1]:
        return 'Ваше слово полиндром'
    else:
       return 'Ваше слово не полиндром'

print('Для выхода наберите "stop"')
while True:
    x = input('Введите слово: ')
    if x == 'stop':
        print('Программа завершилась')
        break
    else:
        print(foo(x))