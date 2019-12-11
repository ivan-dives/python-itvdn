# Задание
# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

class Cars:

    def __init__(self, car_new, color_new, maxspeed_new):
        self.car = car_new
        self.color = color_new
        self.maxspeed = maxspeed_new

    def __str__(self):
        return f'Марка Авто: {self.car}\n' \
               f'Цвет: {self.color}\n' \
               f'Максимальная скорость: {self.maxspeed}'

    def __repr__(self):
        return f'Марка Авто: {self.car}; ' \
               f'Цвет: {self.color}; ' \
               f'Максимальная скорость: {self.maxspeed}'

car1 = Cars('Ford', 'Black', 320)
car2 = Cars('Mazda', 'Red', 240)
print(car1)
print()
print(car2)
print()

class Market():

    def price(self, price_new):
        self.price = price_new

p1 = Market()
p1.price(30000)

p2 = Market()
p2.price(20000)

list = [car1.car, p1.price, car2.car, p2.price]
print(list)