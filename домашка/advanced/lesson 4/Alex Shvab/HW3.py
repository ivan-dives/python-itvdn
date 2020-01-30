def to_file(name, bases, _dict):
    print(name, bases, _dict)
    with open("class.txt", "w") as file:
        result = str(name) + "\n"
        result += str(bases) + "\n"
        for x in _dict.items():
            result += str(x) + "\n"
        file.write(result)






class Car(metaclass=to_file):
    def __init__(self, speed=10):
        self.speed = speed

    def SET_SPEED(self, new_speed):
        self.speed = new_speed

    def GET_SPEED(self):
        return self.speed