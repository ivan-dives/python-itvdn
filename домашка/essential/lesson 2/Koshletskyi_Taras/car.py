#!/usr/bin/python3
# -*- coding: utf-8 -*_


import vehicle


class Car(vehicle.Vehicle):

    __current_capacity = 0

    def __init__(self, maker, model, color, year, capacity, max_speed):
        self.__max_capacity = capacity
        self.__max_speed = max_speed
        super().__init__(maker, model, color, year, self.__max_speed)

    def pick_up(self, passangers):
        if passangers <=0:
            print("Take normal passengers")
        elif passangers > (self.__max_capacity - self.__current_capacity):
            print("Take a bus")
        else:
            print(f"Take {passangers} passangers")
            self.__current_capacity += passangers

    def get_current_capacity(self):
        return self.__current_capacity

    def drop_off(self, passangers):
        self.__current_capacity -= passangers
