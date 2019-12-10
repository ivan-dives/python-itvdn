class Printer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *param):
        self.func(*param)


@Printer
class Vehicle:
    def __init__(self, wheels=4, transport="Средство передвижения"):
        self.wheels = wheels
        self.transport = transport

    def go(self):
        print(f"{self.transport} на {self.wheels} колёсах")

@Printer
class Car(Vehicle):
    def __init__(self, wheels=4, engine=1, transport="Машина"):
        self.wheels = wheels
        self.transport = transport
        self.engine = engine

    def go(self):
        print("Поехали")
        print(f"{self.transport} на {self.wheels} колесах и {self.engine} двигателем")

@Printer
class Bus(Car):
    def __init__(self, wheels=4, passengers=9, engine=1, transport="Автобус"):
        self.wheels = wheels
        self.transport = transport
        self.engine = engine
        self.passengers = passengers

    def go(self):
        print("Поехали")
        print(f"{self.transport} на {self.wheels} кольосах и {self.engine} \
        перевозящий {self.passengers} пасажиров")

@Printer
class Boat(Vehicle):
    def __init__(self, wheels=0, passengers=2, transport="Лодка"):
        self.wheels = wheels
        self.transport = transport
        self.passengers = passengers


    def go(self):
        print("Кузмич бери весла и греби")
        print(f"{self.transport} на {self.wheels} кольосами и перевозящий {self.passengers} пасажиров")


@Printer
class Plane(Vehicle):
    def __init__(self, wings=2, passengers=50, engine=2, transport="Самолет"):
        self.wings = wings
        self.transport = transport
        self.passengers = passengers
        self.engine = engine

    def go(self):
        print("Полетели")
        print(f"{self.transport} с {self.wings} крыльями, {self.engine} двигателей, и перевозящий {self.passengers} пасажиров")


reno = Car()
reno.go()
boing = Plane()
boing.go()
rubber_boat = Boat()
rubber_boat.go()