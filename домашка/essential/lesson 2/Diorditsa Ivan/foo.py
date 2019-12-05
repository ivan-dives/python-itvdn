
class Square(IsoscelesShape):
    def draw(self):
        for _ in range(self.side):
            print('*' * self.side)

s =

exit()

class Parent:
    def whoami(self):
        print("I am parent")
        super().whoami()


class Child:
    def whoami(self):
        print("I am child")
        print("now I'll ask my parent")
        #Parent.whoami(None)


c = Child()
c.whoami()
exit()

class UnpaidVersion:
    def edit_document(self):
        print("cannot edit, please buy")

class PaidVersion(UnpaidVersion):
    def edit_document(self):
        print("ok, I am paid version")

p = input("please enter password ")
editor = PaidVersion() if p == '123' else UnpaidVersion()
editor.edit_document()

exit()


class Klass:
    __temp = 10

    def __init__(self, temp=20):
        self.__temp = temp

    def get_temp(self):
        return self.__temp

c = Klass()
print(c.get_temp())

exit()

class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        tmp = self.get_temperature()
        tmp *= 1.8
        tmp += 32
        return tmp
        #return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        self._temperature = value

c = Celsius()
f = c.to_fahrenheit()
print(f)

exit()


class C:
    tmp = [10]

class Klass:
    tmp = [10]

    #def __init__(self, newtmp=20):
    #    self.tmp = [newtmp]
    #    self.tmp = 20

    def __init__(self, new_tmp):
        #new_tmp = 20
        self.new_tmp = tmp

c = Klass(40)
print(id(c.tmp))
print(c.tmp)
print(c.new_tmp)
d = Klass(40)
print(id(d.tmp))
print(d.tmp)

exit()

#c = C()
#c.tmp.append(20)
#d = C()
#print(d.tmp)

#exit()

c = Klass()
print(id(c.tmp))
d = Klass()
print(id(d.tmp))
e = Klass()
print(id(e.tmp))
print(id(Klass.tmp))

exit()

class Vehicle:
    color = 'white'

    def __init__(self, new_color='white'):
        self.color = new_color

class Car(Vehicle):
    speed = 30

    def __init__(self, new_speed):
        self.speed = new_speed

        super().__init__()

c = Car(10)
print(c.speed, c.color)

exit()

class MyInt(int):
    def __truediv__(self, other):
        if isinstance(other, str):
            other = int(other)
        return super().__truediv__(other)
        #return int.__truediv__(self, other)

i = MyInt(10)
print(i / "10")
#print(i / 10)

exit()

class Car:
    speed = 0

    def change_speed(self, new_speed):
        print('поменять скорость')
        self.speed = new_speed

class Truck(Car):
    def change_speed(self, new_speed):
        print('моргнуть фарами')
        #Car.change_speed(self, new_speed)
        super().change_speed(new_speed)

t = Truck()
t.change_speed(10)

exit()

class Car:
    speed = 0

    def change_speed(self, new_speed):
        self.speed = new_speed

class Surface:
    color = 'white'

    def __init__(self, new_color='white'):
        self.color = new_color

class Truck(Car, Surface):
    capacity = 3000 # kilo


print(Truck.__mro__)
t = Truck()
exit()

#t = Truck()

#print(Truck.__mro__)
#print(int.__mro__)
#print(bool.__mro__)

#o = object()


#print(t.capacity)
#print(t.speed)
#t.change_speed(10)
#t.speed = 10
#print(f'{t.speed}')
#print(f'{Car.speed}')

# MRO

one = Truck()
print(isinstance(one, Truck), one, Truck)
#print(isinstance(Truck, Car))
print(issubclass(Truck, Car))
print(id(Car))
#two = Truck()

#Car.speed = 100
#print(one.speed)
#print(two.speed)


