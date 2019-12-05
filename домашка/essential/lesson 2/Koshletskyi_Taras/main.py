#!/usr/bin/python3
# -*- coding: utf-8 -*_

import car
import bus


def main():

    bmw = car.Car("bmw", "535", "black", 2018, 4, 250)
    bmw.turn_on()
    bmw.set_speed(210)
    bmw.pick_up(0)
    bmw.pick_up(4)
    bmw.pick_up(1)
    bmw.turn_off()
    print(bmw.get_current_capacity())
    print(bmw)

    laz = bus.Bus("LAZ", "Ukraine", "Yellow", 1990, 60, 120 )
    print(laz)


if __name__ == '__main__':
    main()