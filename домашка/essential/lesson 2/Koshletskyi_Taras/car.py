#!/usr/bin/python3
# -*- coding: utf-8 -*_


import vehicle


def wrapper_print(func):

    def wrap(self, *args):
        if not args:
            print("no args")
        for arg in args:
            print(f"arg={arg}", end=", ")
        print()
        res = func(self, *args)
        if res:
            print(f"Return: {res}")
        else:
            print("return nothing")
        return res

    return wrap



class Car(vehicle.Vehicle):

    __current_capacity = 0

    @wrapper_print
    def __init__(self, maker, model, color, year, capacity, max_speed):
        self.maker = maker
        self.model = model
        self.color = color
        self.year = year
        self.__max_capacity = capacity
        self.__max_speed = max_speed
        super().__init__(self.__max_speed)

    @wrapper_print
    def pick_up(self, passengers):
        if passengers <=0:
            print("Take normal passengers")
        elif passengers > (self.__max_capacity - self.__current_capacity):
            print("Take a bus")
        else:
            print(f"Take {passengers} passengers")
            self.__current_capacity += passengers

    @wrapper_print
    def get_current_capacity(self):
        return self.__current_capacity

    def drop_off(self, passengers):
        self.__current_capacity -= passengers


    def __str__(self):
        return super().__str__() + \
                f"Maker: {self.maker}, " \
                f"Model: {self.model}, " \
                f"Сolor: {self.color}, " \
                f"Produced in {self.year} " \

