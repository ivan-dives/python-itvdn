# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.

import math

def addition(a, b):
    x = a + b
    return x

def subtraction(a, b):
    x = a - b
    return x

def multiplication(a, b):
    x = a * b
    return x

def division(a, b):
    try:
        x = a / b
        return x
    except:
        pass


while True:
    print('''
    1. Калькулятор
    2. Доп. операции калькулятора
    3. Выход
    ''')

    choise =(input('Сделайте выбор: '))
    print()

    while choise == '1':
        try:
            a = float(input('Введите значение №1: '))
            oper = input('Введите действие +, -, *, /: ')
            if oper != '+' and oper != '-' and oper != '*' and oper != '/':
                continue
            b = float(input('Введите значение №2: '))
            print()
        except:
            print()
            print('Ошибка: Ввод некорректных данных')
            continue

        if oper == '+':
            print(f'Ответ: {float(addition (a, b))}')
            print('''
                        1. Продолжить
                        2. Выход
            ''')
            choise2 = input()
            if choise2 == '1':
                continue
            elif choise2 == '2':
                break
        elif oper == '-':
            print(f'Ответ: {float(subtraction (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise2 = input()
            if choise2 == '1':
                continue
            elif choise2 == '2':
                break
        elif oper == '*':
            print(f'Ответ: {float(multiplication (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise2 = input()
            if choise2 == '1':
                continue
            elif choise2 == '2':
                break
        elif oper == '/':
            print(f'Ответ: {(division (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise2 = input()
            if choise2 == '1':
                continue
            elif choise2 == '2':
                break
        else:
            print("Неправильный ввод, подторите!")
            input('Press ENTER')
            break

    if choise == '2':
        print('''
            1. Возведение в степень
            2. Синус
            3. Косинус
            4. Тангенс
            5. Выход
        ''')

        choice2 = input('Сделайте выбор: ')

        if choice2 == '1':
            try:
                a = float(input('Введите значение: '))
                b = float(input('Введите степень: '))
                z = a ** b
                z = round(z, 3)
                print()
                print(f'{a} в степени {b} = {z}')
            except ZeroDivisionError:
                print()
                print('Ошибка: Возведении нуля в отрицательную степень')
                pass
            except ValueError:
                print()
                print('Ошибка: Ввод некорректных данных')
                pass

        elif choice2 == '2':
            a = float(input('Введите значение: '))
            z = math.sin(a)
            z = round(z, 3)
            print()
            print(f'sin({a}) = {z}')

        elif choice2 == '3':
            a = float(input('Введите значение: '))
            z = math.cos(a)
            z = round(z, 3)
            print()
            print(f'cos({a}) = {z}')

        elif choice2 == '4':
            a = float(input('Введите значение: '))
            z = math.tan(a)
            z = round(z, 3)
            print()
            print(f'tan({a}) = {z}')

        elif choice2 == '5':
            print('ВЫХОД')


    if choise == '3':
        break
