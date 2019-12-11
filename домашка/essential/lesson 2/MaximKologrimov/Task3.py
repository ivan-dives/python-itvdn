# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран
# порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
# классов выглядят именно так.

class Village:
    pass

class Trade(Village):
    pass

class Warehouse(Village):
    pass

class Metal(Trade):
    pass

class Wood(Trade, Warehouse):
    pass

class Food(Warehouse):
    pass

class Lumberjacks(Wood, Food, Metal):
    pass

class Blacksmiths(Metal, Food):
    pass

class Hunters(Food, Metal):
    pass

def main():
    print(Village.mro())
    print()
    print(Trade.mro())
    print()
    print(Warehouse.mro())
    print()
    print(Metal.mro())
    print()
    print(Wood.mro())
    print()
    print(Food.mro())
    print()
    print(Lumberjacks.mro())
    print()
    print(Blacksmiths.mro())
    print()
    print(Hunters.mro())

if __name__ == '__main__':
    main()