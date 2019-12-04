class Vehicle:
    def __init__(self, wheels=4, carcase="Доска"):
        self.wheels = wheels
        self.carcase = carcase

    def go(self):
        print(f"{self.carcase} на {self.wheels} колёсах")

class Car(Vehicle):
    def __init__(self, wheels=4, engine=1, carcase="Кузов"):
        self.wheels = wheels
        self.carcase = carcase
        self.engine = engine

    def go(self):
        print(f"{self.carcase} на {self.wheels} колесах и {self.engine} двигателем")

class Bus(Car):
    def __init__(self, wheels=4, passengers=9, engine=1, carcase="Кузов"):
        self.wheels = wheels
        self.carcase = carcase
        self.engine = engine
        self.passengers = passengers

    def go(self):
        print(f"{self.carcase} на {self.wheels} и {self.engine} перевозящий {self.passengers} пасажиров")