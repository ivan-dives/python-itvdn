class Car:
    def __init__(self, model, engine, transmission, mileage, year):
        self.model = model
        self.engine = engine
        self.transmission = transmission
        self.mileage = mileage
        self.year = year

    def info(self):
        print(f'model - {self.model}\nengine volume - {self.engine}\ntransmission - {self.transmission}\nmileage - {self.mileage}\nyear of issue - {self.year}')

class Audi(Car):
    a = Car('Audi', 2.0, 'mechanic', 218000, 2012)
    a.info()
    print()

class Toyota(Car):
    t = Car('Toyota', 1.6, 'automatic', 164000, 2016)
    t.info()
    print()

class Renault(Car):
    r = Car('Renault', 1.8, 'automatic', 127000, 2015)
    r.info()