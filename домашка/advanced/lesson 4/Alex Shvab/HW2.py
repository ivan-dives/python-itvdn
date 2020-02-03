def checker(name, bases, _dict):
    print(name, bases, _dict)
    newdict = {}
    for k, v in _dict.items():
        for i in k:
            if not i.isdigit():
                raise Exception("Name can't include numbers")
        if not k.islower():
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