class Ts:
    def __init__(self, color, weight, speed, passengers, fuel):
        self.color = color
        self.weight = weight
        self.speed = speed
        self.passengers = passengers
        self.fuel = fuel


class Auto(Ts):
    __wheels = 4
    __license_category = "B"

    def __init__(self, color, weight, speed, passengers, fuel, engine):
        super().__init__(color, weight, speed, passengers, fuel)
        self.engine = engine

    def description(self):
        print(f"легковой автомобиль, {self.__wheels}х колёсное транспортное средство, {self.color}"
              f" цвета, двигаться со скоростью {self.speed} весом примерно {self.weight}, заправлено "
              f"{self.fuel}, может перевозить {self.passengers}, имеет {self.engine}, требует права "
              f"категории {self.__license_category}")


class Moto(Auto):
    __wheels = 2
    __license_category = "A"

    def __init__(self, color, weight, speed, passengers, fuel, engine):
        super().__init__(color, weight, speed, passengers, fuel, engine)

    def description(self):
        print(f"мотоцикл, {self.__wheels}х колёсное транспортное средство, {self.color} цвета, двигаться со скоростью "
              f"{self.speed} весом примерно {self.weight}, заправлено {self.fuel}, может перевозить {self.passengers},"
              f" имеет {self.engine}, требует права категории {self.__license_category}")


class Velo(Ts):
    __wheels = 2
    __fuel = "Человеком"

    def __init__(self, color, weight, speed, passengers):
        super().__init__(color, weight, speed, passengers, fuel=None)

    def description(self):
        print(f"велосипед, {self.__wheels}х колёсное транспортное средство, {self.color} цвета, двигаться со скоростью "
              f"{self.speed} весом примерно {self.weight}, заправлено {self.__fuel}, может перевозить "
              f"{self.passengers}")


def main():
    color = input("Введите цвет транспорта:\n>> ")
    weight = input("Введите примерный вес транспортного средства:\n>> ")
    speed = input("Введите скорость транспорта:\n>> ")
    passengers = int(input("Введите количество возможных пассажиров:\n>> "))
    auto = Auto(color, weight, speed, passengers, fuel="Топлевом", engine="ДВС")
    moto = Moto(color, weight, speed, passengers, fuel="Топлевом", engine="ДВС")
    velo = Velo(color, weight, speed, passengers)
    if 2 < passengers < 4:
        print(f"Вам подойдет {auto.description()}")
    elif passengers == 4:
        print(f"Вам подойдет {auto.description()}, но ехать будет тесно")
    elif passengers == 1:
        print(f"Вам подойдет {velo.description()}\nили при наличии прав\n{moto.description()}")
    else:
        print("Едьте на маршруике или такси...")


if __name__ == '__main__':
    main()
