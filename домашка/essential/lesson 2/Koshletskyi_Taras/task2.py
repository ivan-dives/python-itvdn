#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Field:

    __shapes = []

    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height


    def draw_shape(self, shape):
        if shape.a >= 0 and shape.a < self.width and shape.b >= 0 and shape.b < self.width:
            self.__shapes.append(shape)
            shape.draw()
        else:
            print("Insert correct point")

    def click_mouse(self, point):
        for shape in self.__shapes:
            if point.a >= shape.a and point.a <= shape.b:
                point.input()
            else:
                print("Mimo")

class Shape:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"Draw shape with a : {self.a}, b {self.b}")


class Mouse:

    def __init__(self, a):
        self.a = a

    def input(self):
        print(f"Input point {self.a}")


def main():
    field = Field()
    shape = Shape(0, 20)
    field.draw_shape(shape)
    point = Mouse(10)
    point2 = Mouse(30)
    field.click_mouse(point)
    field.click_mouse(point2)


if __name__ == '__main__':
    main()