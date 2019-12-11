import math

print('''
    1. Обычный калькулятор
    2. Доп. операции калькулятора
    3. Выход
''')

choice = input('Сделайте выбор: ')

z = None

if choice == '1':
    while z == None:
        a = float(input('Введите значение: '))
        oper = input('Введите действие +, -, *, /: ')
        b = float(input('Введите значение: '))

        if oper == '+':
            z = a + b
            print('Ответ: ' + str(z))
        elif oper == '-':
            z = a - b
            print('Ответ: ' + str(z))
        elif oper == '*':
            z = a * b
            print('Ответ: ' + str(z))
        elif oper == '/':
            z = a / b
            print('Ответ: ' + str(z))
        else:
            print("Неправильный ввод, подторите!")

if choice == '2':
    print('''
        1. Возведение в степень
        2. Синус
        3. Косинус
        4. Тангенс
        5. Выход
    ''')

    choice2 = input('Сделайте выбор: ')

    if choice2 == '1':
        a = float(input('Введите значение: '))
        b = float(input('Введите степень: '))
        z = a**b
        z = round(z, 3)
        print()
        print(f'{a} в степени {b} = {z}')

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

if choice == '3':
    print('ВЫХОД')
