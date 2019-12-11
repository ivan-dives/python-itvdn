# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

# +
def plus(x1, x2):
    return x1 + x2


# -
def minus(x1, x2):
    return x1 - x2


# *
def multiplication(x1, x2):
    return x1 * x2


# /
def div(x1, x2):
    if x2 == 0:
        return
    else:
        return x1 / x2


def main():
    while True:
        op = input("Введите опреацию: ")
        if op.lower() == "exit":  # выход
            return
        elif op == "+":  # сложение
            x1 = input("Введите первое число x1 = ")
            x1 = float(x1)
            x2 = input("Введите второе число x2 = ")
            x2 = float(x2)
            print("{} + {} = {}".format(x1, x2, plus(x1, x2)))
        elif op == "-":  # сложение
            x1 = input("Введите первое число x1 = ")
            x1 = float(x1)
            x2 = input("Введите второе число x2 = ")
            x2 = float(x2)
            print("{} - {} = {}".format(x1, x2, minus(x1, x2)))
        elif op == "*":  # умножение
            x1 = input("Введите первое число x1 = ")
            x1 = float(x1)
            x2 = input("Введите второе число x2 = ")
            x2 = float(x2)
            print("{} * {} = {}".format(x1, x2, multiplication(x1, x2)))
        elif op == "/":  # деление
            x1 = input("Введите первое число x1 = ")
            x1 = float(x1)
            x2 = input("Введите второе число x2 = ")
            x2 = float(x2)
            res = div(x1, x2)
            if res:
                print("{} / {} = {}".format(x1, x2, res))
            else:
                print("Нельзя делить на ноль!")
        else:
            print("Некорректная операция!")


if __name__ == '__main__':
    main()
