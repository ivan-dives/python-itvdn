def Calculator():
    while True:
        operation = input("Введите операцию (+, -, *, /, **) "
                          "или для выхода - exit: ")
        if operation == 'exit':
            break
        else:
            try:
                number_x = float(input('Введите число х: '))
                number_y = float(input('Введите число y: '))
            except ValueError:
                print('Не верно введено значение, повторите пожалуйста')
                continue
        if operation == '+':
            return number_x + number_y
        elif operation == '-':
            return number_x - number_y
        elif operation == '*':
            return number_x * number_y
        elif operation == '/':
            try:
                return number_x / number_y
            except ZeroDivisionError:
                print('Деление на 0 запрещено, проверте данные')
        elif operation == '**':
            try:
                return number_x ** number_y
            except ZeroDivisionError:
                print('Возведение 0 в отрицательную степень невозможно, проверте данные')
        else:
            print('Некоректно введена операция, повторите пожалуйста')


print(Calculator())
