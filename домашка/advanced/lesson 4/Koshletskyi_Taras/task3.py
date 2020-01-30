# Создайте метакласс, записывающий в файл всю информацию о классах, которые используют его в качестве метакласса.

import json


def write_info(class_name, base_class, attr):
    new_attr = {}
    for k,v in attr.items():
        new_attr[str(k)] = str(v)
    with open(f"class_{class_name}", 'w') as file:
        json.dump(new_attr, file, indent="    ")


class Car(metaclass=write_info):
    def __init__(self, speed=10):
        self.speed = speed

    def SET_SPEED(self, new_speed):
        self.speed = new_speed

    def GET_SPEED(self):
        return self.speed