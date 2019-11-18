import math
print('Выберите операцию')
t = '\n1.Сложение. \n2.Вычитание.\n3.Умножение.\n4.Деление.\n5.Возведения в степень.\n6.Синус.\n7.Косинус.\n8.Тангенс.'
print(t)
number_op = int(input('_'))
if number_op == 1:
    print('Введите два числа')
    x,y = map(int,input().split())
    print(x+y)
elif number_op == 2:
    print('Введите два числа')
    x,y = map(int,input().split())
    print(x-y)
elif number_op == 3:
    print('Введите два числа')
    x,y = map(int,input().split())
    print(x*y)
elif number_op == 4:
    print('Введите два числа')
    x,y = map(int,input().split())
    print(x/y)
elif number_op == 5:
    print('Введите два числа. 1-е число которое хотите возвести в степень и 2-е степень')
    x, y = map(int, input().split())
    print(x**y)
elif number_op == 6:
    print('Введите одно число')
    x = int(input())
    print(math.sin(x))
elif number_op == 7:
    print('Введите одно число')
    x = int(input())
    print(math.cos(x))
elif number_op == 8:
    print('Введите одно число')
    x = int(input())
    print(math.tan(x))
else:
    print('Что-то пошло не так. Попробуейте еще раз нужно ввести от 1 до 8 включительно')
    print(t)
    number_op = int(input('_'))