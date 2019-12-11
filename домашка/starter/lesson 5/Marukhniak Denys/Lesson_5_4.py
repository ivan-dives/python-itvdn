# Задание
# Создайте программу, которая состоит из функции, которая принимает три числа и возвращает
# их среднее арифметическое, и главного цикла, спрашивающего у пользователя числа и
# вычисляющего их средние значения при помощи созданной функции.


def value(z, x, c):
    return (z+x+c)/3


while True:
    z = int(input('First number: '))
    x = int(input('Second number: '))
    c = int(input('Third number: '))
    print('({}+{}+{})/3 = {:.2f}'.format(z, x, c, value(z, x, c)))

    while True:
        again = input('Do you want to do another operation (y/n)? ')
        if again.lower() == 'y':
            break
        elif again.lower() == 'n':
            break
        else:
            print('You have entered a wrong operation, try again')
    if again.lower() == 'n':
        break
