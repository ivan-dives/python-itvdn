# Задание 2
# Напишите программу - калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и возведение
# в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных, делении на ноль и
# возведении нуля в отрицательную степень.
from cmath import *

def sum(a,b):
    print(a+b)

def subtraction(a,b):
    print(a-b)

def multiplication(a,b):
    print(a*b)

def power(a,b):
    try:
        print(a ** b)
    except ZeroDivisionError:
        print('can not raise zero to a minus degree')

def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print ('cannot be divided by zero')


while True:
    z = input('|+|-|/|*|**|exit|')
    if z == 'exit':
        break
    a = int(input('first number'))
    b = int(input('second number'))
    if z == '+':
        sum(a,b)
    elif z == '-':
        subtraction(a,b)
    elif z == '**':
        power(a,b)
    elif z == '*':
        multiplication(a,b)
    elif z == '/':
        division(a,b)
    else:
        print('choose one of these characters |+|-|/|*|exit|')