def checker(name, bases, _dict):
    print(name, bases, _dict)
    newdict = {}
    for k, v in _dict.items():
        if [s for s in k if s in '1234567890']:
            raise Exception("Name can't include numbers",)
        if k.isupper():
            raise Exception("Name can't include upper case")
        newdict[k.lower()] = v
    print(name, bases, newdict)
    return type(name, bases, newdict)



# class Car(metaclass=checker):
#     def __init__(self, speed=10):
#         self.speed = speed
#
#     def SET_SPEED(self, new_speed):
#         self.speed = new_speed
#
#     def GET_SPEED(self):
#         return self.speed



# class Bus(metaclass=checker):
#     def __init__(self, speed=10):
#         self.speed = speed
#
#     def hate_speed1(self):
#         self.speed = 0

class Boat(metaclass=checker):
    def __init__(self, speed=10):
        self.speed = speed

    def love_speed(self):
        self.speed = 100