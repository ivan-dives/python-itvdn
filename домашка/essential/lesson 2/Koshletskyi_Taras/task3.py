#!/usr/bin/python3
# -*- coding: utf-8 -*_


class A:

    def __init__(self):
        print(f' {type(self)} in conctructor A')


    def takoe(self):
        print("in Class A")


class B(A):

     def __init__(self):
        super().__init__()
        print(f'{type(self)} in conctructor B')

     def takoe(self):
        print("in Class B")




class C(A):

    def __init__(self):
        super().__init__()
        print(f' {type(self)} in conctructor C')

    def takoe(self):
        print("in Class C")


class D(B, C):

    def __init__(self):
        super().__init__()
        print(f' {type(self)} in conctructor D')



def main():
    d = D()
    d.takoe()
    for cls in [A, B, C, D]:
        print(cls, cls.mro())


if __name__ == '__main__':
    main()

