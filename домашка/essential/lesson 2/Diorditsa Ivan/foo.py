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


