def foo(name, bases, _dict):
    print(name, bases, _dict)
    newdict = {}
    for k, v in _dict.items():
        newdict[k.lower()] = v
    print(name, bases, newdict)
    return type('name+1', bases, newdict)


#def foo(*args):
#    return None


class Car(metaclass=foo):
    def __init__(self, speed=10):
        self.speed = speed

    def SET_SPEED(self, new_speed):
        self.speed = new_speed

    def GET_SPEED(self):
        return self.speed

#class ChildCar(Car):
#    pass

#print('ChildCar', dir(ChildCar))

print(type(Car))
car = Car()
print(dir(car))
print(type(Car), type(car), Car.__name__)

exit()

def myinit(cls, speed=10):
    cls.speed = speed

# metaprogramming
Car = type('Car', (object,), dict(__init__ = myinit, x = 20))

car = Car()
print(type(car), type(Car))
print(car.speed)

exit()


class Car(object):
    x = 20

    def __init__(self, speed=10):
        self.speed = speed


car = Car()
print(type(car), type(Car))
