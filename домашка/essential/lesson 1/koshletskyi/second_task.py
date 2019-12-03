#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Disgusting:

    def __init__(self, name, mass, high):
        self.name = name
        self.mass = mass
        self.high = high
        print("Hello bitch =)")

    def __str__(self):
        return f"I am Disgusting {self.name}, my mass is {self.mass} and my len is {self.__len__()}"

    def __len__(self):
        return self.high

    def __add__(self, other):
        return self.mass + other.mass

    def __sub__(self, other):
        return self.mass - other.mass

    def __mul__(self, other):
        return self.mass * other.mass

    def __eq__(self, other):
        return self.name == other.name \
            and self.mass == other.mass \
            and self.high == other.high

    def __bool__(self):
        return self.name.strip() !="" \
               and self.mass > 0 \
               and self.high > 0

    def __lt__(self, other):
        return self.mass < other.mass

    def __le__(self, other):
        return self.mass <= other.mass

    def __del__(self):
        print("I will be back")

    def __int__(self):
        return self.mass

    def __getattr__(self, item):
        if item == "supper":
            return "I will kill everyone"
        else:
            return "Let's be a friend"


def main():
    dis = Disgusting("Mraz", 148, 740)
    # dis1 = Disgusting("Tvar", 841, 18)
    # dis2 = Disgusting("Tvari", 841, 18)
    # dis3 = Disgusting("Q ", 0, 18)

    # if dis3:
    #     print(dis3)
    # else:
    #     print("Dno")

    # print(dis)
    # print(len(dis))
    # print(dis+dis1)
    # print(dis1 < dis2)


if __name__ == '__main__':
    main()

