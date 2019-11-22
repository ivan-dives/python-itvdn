# Задание 3
# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.


def calc(operation, b, c):
    if operation == '-':
        a = b - c
        return a
    elif operation == '+':
        a = b + c
        return a
    elif operation == '*':
        a = b * c
        return a
    elif operation == '/':
        a = b / c
        if c == 0:
            return "Please, don't try dividing the number by zero"
        else:
            return a


while True:
    b = int(input('First number: '))
    c = int(input('Second number: '))
    operation = input('Input your operation: ')
    print(f'{b} {operation} {c} = {calc(operation, b, c)}')

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
