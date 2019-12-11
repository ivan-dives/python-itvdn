#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Vehicle:

    __count_number = 0

    def __init__(self, max_speed=80):
        self.__speed = 0
        self.__engine = False
        self.__max_speed = max_speed
        Vehicle.__count_number += 1

    def get_engine(self):
        return "Engine is working" if self.__engine else "Engine is stopped"

    def turn_on(self):
        if not self.__engine:
            print("Turn on engine")
            self.__engine = True
        else:
            print("Engine is working")

    def turn_off(self):
        if self.__engine:
            print("Turn off engine")
            self.__engine = False
        else:
            print("Engine is not working")

    def set_speed(self, speed):
        if self.__engine:
            if speed > self.__max_speed or speed < 0:
                print("I can't set this speed")
            else:
                print(f"Set speed {speed}")
                self.__speed = speed
        else:
            print("Please turn on engine")

    def __str__(self):
        return f"This is a type {self.__class__.__name__} of Vehicle, My {self.get_engine()}, " \
               f"my max speed is {self.__max_speed} "



