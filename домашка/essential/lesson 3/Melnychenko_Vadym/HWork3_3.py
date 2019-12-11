class Excep(Exception):
    pass


class Person:
    employee = []

    def __init__(self, name, surname, department, in_year):
        self.name = name
        self.surname = surname
        self.department = department
        self.in_year = in_year

    def __str__(self):
        return print(Person.employee)


def employ():
    first_name = input('Введите имя: ')
    if len(first_name) < 3:
        raise Excep
    last_name = input('Введите фамилию: ')
    if len(last_name) < 4:
        raise Excep
    otdel = input('Введите отдел: ')
    year = int(input('Введите год: '))
    return Person.employee.append(f'{first_name}, {last_name}, {job_title}, {year}')


def foo():
    try:
        employ()
        c = Person
        print(c.employee)
    except Excep:
        print('ошибка')


foo()
