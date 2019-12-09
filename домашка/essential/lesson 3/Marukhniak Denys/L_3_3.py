# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
# поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
# данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
# после заданного года.
import datetime


class IncorrectYearOfEmployment(BaseException):
    pass


def incorrect_year(year_check):
    if year_check > datetime.date.today().year:
        ex_year = IncorrectYearOfEmployment('Error')
        raise ex_year
    return year_check


class Employee:
    def __init__(self, first_name, second_name, department, year_of_employment):
        self.f_name = first_name
        self.s_name = second_name
        self.dep = department
        try:
            self.year = incorrect_year(year_of_employment)
        except IncorrectYearOfEmployment as ex_year:
            print('This year has not come. Enter year of employment again: ', end=' ')
            while True:
                try:
                    year_of_employment = int(input())
                    self.year = incorrect_year(year_of_employment)
                    break
                except ValueError and IncorrectYearOfEmployment as ex_year:
                    print('Incorrect data, try again.')

    def __repr__(self):
        return f"First name: {self.f_name}\n" \
               f"Second name: {self.s_name}\n" \
               f"Department: {self.dep}\n" \
               f"Year of employment: {self.year}\n"


employees = []
count = int(input('How many employees you need to add? '))

while count:
    try:
        f_name = input('Enter first name: ')
        s_name = input('Enter second name: ')
        dep = input('Enter department: ')
        year = int(input('Enter year of employment: '))
        new_employee = Employee(f_name, s_name, dep, year)
    except ValueError as ex_num:
        print('Incorrect data for year, try again.')
    else:
        employees.append(new_employee)
        count -= 1
    finally:
        print()

while True:
    try:
        chosen_year = int(input('From what year do you want to display employees? '))
        break
    except ValueError as ex_num:
        print('Incorrect data, try again.')

nth = 0
for employee_id in employees:
    if employee_id.year >= chosen_year:
        nth = 1
        print(employee_id)
if nth == 0:
    print(f'None of the employees were hired after {chosen_year} year')
