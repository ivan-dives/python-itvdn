# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран
# порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
# классов выглядят именно так.


class Car:
    max_speed = 150  # k/h

    def __str__(self):
        return f'{self.max_speed=}'


class House:
    capacity = 6  # people

    def __str__(self):
        return f'{self.capacity=}'


class CamperVan(Car, House):
    max_speed = 120
    capacity = 4

    def __str__(self):
        return f'{self.capacity=}, {self.max_speed=}'


volvo = Car()
flat = House()
fiat = CamperVan()

print(volvo)
print(flat)
print(fiat)

print(Car.__mro__)
print(House.__mro__)
print(CamperVan.__mro__)
