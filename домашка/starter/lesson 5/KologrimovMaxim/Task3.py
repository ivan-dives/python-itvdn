# Задание 3
# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

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
    if b == 0:
        return print('На ноль дель нелзя\n')
    else:
        x = a / b
        return x

while True:
    print('''
    1. Калькулятор
    2. Выход
    ''')

    choise =(input('Сделайте выбор: '))
    print()

    while choise == '1':
        a = float(input('Введите значение №1: '))
        oper = input('Введите действие +, -, *, /: ')
        if oper != '+' and oper != '-' and oper != '*' and oper != '/':
            break
        b = float(input('Введите значение №2: '))
        print()

        if oper == '+':
            print(f'Ответ: {float(addition (a, b))}')
            print('''
            1. Продолжить
            2. Выход
            ''')
            choise = input()
            if choise == '1':
                continue
            elif choise == '2':
                break
        elif oper == '-':
            print(f'Ответ: {float(subtraction (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise = input()
            if choise == '1':
                continue
            elif choise == '2':
                break
        elif oper == '*':
            print(f'Ответ: {float(multiplication (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise = input()
            if choise == '1':
                continue
            elif choise == '2':
                break
        elif oper == '/':
            print(f'Ответ: {(division (a, b))}\n')
            print('''
                        1. Продолжить
                        2. Выход
                        ''')
            choise = input()
            if choise == '1':
                continue
            elif choise == '2':
                break
        else:
            print("Неправильный ввод, подторите!")
            input('Pres ENTER')
            break

    if choise == '2':
        break