# Задание
# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
# транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
# Выведите информацию о каждом транспортном средстве.

class Cars:
    speed = 0

    def change_speed(self, speed_new):
        self.speed = speed_new

    def __init__(self, speed_slow):
        self.speed = speed_slow

    def __str__(self):
        return f'Скорость TestCar: {self.speed}'

class Faster(Cars):

    def spec(self, color_new):
        self.color = color_new

    def __str__(self):
        return f'Цвет: {self.color}'

class Lux(Faster):

    def sum(self, price_new):
        self.price = price_new

class Heavy(Lux):

    def germ_car(self,car_new):
        self.car = car_new

class Light(Faster):

    def jap_car(self,car_new):
        self.car = car_new

class OldCar(Cars):
    pass


test_car = Cars(100)
print(f'TestCar {id(test_car)}, {test_car}')
print('* * * * * * * * * * * * * * * * * * * * * * * *')
mazda = Light(Faster)
mazda.change_speed(200)
mazda.spec('Black')
#mazda.sum(100000)
print(f'Mazda id {id(mazda.speed)}, {mazda.speed}, {mazda}, {mazda.color}')
print('* * * * * * * * * * * * * * * * * * * * * * * *')

bmw = Heavy(Lux)
bmw.change_speed(340)
bmw.spec('White')
bmw.sum(1000000)
print(f'BMW id {id(bmw.speed)}, {bmw.speed}, {bmw}, {bmw.price}')
print('* * * * * * * * * * * * * * * * * * * * * * * *')

old = OldCar(Cars)
old.change_speed(40)
print(f'OldCar id {id(old)}, {old}')

