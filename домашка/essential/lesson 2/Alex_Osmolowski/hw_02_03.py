# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран
# порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
# классов выглядят именно так.


class Human:
    pass


class Citizen(Human):
    pass


class Position:
    pass


class President(Citizen, Position):
    pass


def main():
    print(Human.mro())
    print(Citizen.mro())
    print(Position.mro())
    print(President.mro())


if __name__ == '__main__':
    main()