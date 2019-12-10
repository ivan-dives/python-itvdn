#!/usr/bin/python3
# -*- coding: utf-8 -*_

class Employee:

    __employes = []

    def __init__(self, name, surname, male, year):
        if not isinstance(name, str):
            raise TypeError
        elif not isinstance(surname, str):
            raise TypeError
        elif not isinstance(male, str):
            raise TypeError
        elif not isinstance(year, int):
            raise TypeError
        else:
            self.name = name
            self.surname = surname
            self.male = male
            self.year = year
            Employee.__employes.append(self)


    def __str__(self):
        return f"{self.name} {self.surname};"

    @staticmethod
    def get_employes():
        return Employee.__employes

    @staticmethod
    def get_employes_year(year):
        lst = []
        for e in Employee.__employes:
            if e.year >= year:
                lst.append(e)
        return lst




def main():
    try:
        em1 = Employee("Taras", "K", "M", 1990)
        em2 = Employee("Denys", "L", "M", 1970)
        em3 = Employee("Andr", "T", "M", 1999)
    except TypeError as error:
        print("Input correct data", error)

    print(*Employee.get_employes())
    print(*Employee.get_employes_year(1990))


if __name__ == '__main__':
    main()
