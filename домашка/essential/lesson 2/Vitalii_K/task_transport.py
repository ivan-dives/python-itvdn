class Vehicle:
    def __init__(self, u = 'transporting'):
        self.usage = u
    def __str__(self):
        return f'used for {self.usage}'

class Motor_Vehicle(Vehicle):
    def __init__(self, t = 'motor vehicle'):
        self.vtype = t
        super().__init__()
    def __str__(self):
        return f'{self.vtype} {super().__str__()}'

class Car(Motor_Vehicle):
    def __init__(self, n = '', st = 'car',w = 4, b = 'land based'):
        self.name = n
        self.subtype = st
        self.wheels = w
        self.vbase = b
        super().__init__()
    def __str__(self):
        return f'{self.name} is a {self.subtype} with {self.wheels} wheels'\
               f'({self.vbase} {super().__str__()})'

class Bike(Motor_Vehicle):
    def __init__(self, n = '', st = 'motorcycle', w =2, b = 'land based'):
        self.name = n
        self.subtype = st
        self.wheels = w
        self.vbase = b
        super().__init__()
    def __str__(self):
        return f'{self.name} is a {self.subtype} with {self.wheels} wheels '\
               f'({self.vbase} {super().__str__()})'

class Motorboat(Motor_Vehicle):
    def __init__(self, n = '', st = 'motorboat', b = 'water based'):
        self.name = n
        self.subtype = st
        self.vbase = b
        super().__init__()
    def __str__(self):
        return f'{self.name} is a {self.subtype} '\
               f'({self.vbase} {super().__str__()})'
class Jet(Motor_Vehicle):
    def __init__(self, n = '', st = 'aircraft', w = 'wings', b = 'air based'):
        self.name = n
        self.subtype = st
        self.wings = w
        self.vbase = b
        super().__init__()
    def __str__(self):
        return f'{self.name} is a {self.subtype} with {self.wings} '\
               f'({self.vbase} {super().__str__()})'


nissan = Car('Nissan GT-R', 'sports car')
mack = Car('Mack Anthem', 'tractor truck', 10)
yamaha = Bike('Yamaha YZF-R3', 'sports bike')
hd = Bike('Harley-Davidson Freewheeler', 'trike motorcycle', 3)
bw = Motorboat('Boston Whaler 380 Realm')
b747 = Jet('Boeing 747', 'jet airliner')
print(nissan, mack, yamaha, hd, bw, b747, sep='\n')
