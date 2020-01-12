import datetime

start_employees = 2000

def range_(year):
    return start_employees <= year <= datetime.date.today().year

class Employee:

    def __init__(self, first_name, second_name, department, work_year):
        if not range_(work_year):
            raise ValueError("Year is out of range, try again")

        self.first_name = first_name
        self.second_name = second_name
        self.departament = department
        self.year = work_year

    def __repr__(self):
        return f"Employee: {self.first_name} {self.second_name} \n" \
               f"Departament: {self.departament}\nStart year: {self.year}"

def main():
    employees = []

    while True:
        print("Enter employees\nTo continue, Enter. To exit, press stop.")
        stop = input("")
        if stop == "stop":
            break
        try:
            first_name = input('Enter first name ')
            second_name = input('Enter second name ')
            department = input('Enter departament ')
            year = int(input('Enter start work year '))
            emp = Employee(first_name, second_name, department, year)
        except ValueError as error:
            print("Error", error)
        else:
            employees.append(emp)
        finally:
            print()

    while True:
        try:
            year = int(input("Enter year: "))
            if not range_(year):
                raise ValueError
            break
        except ValueError:
             print('Incorrect data, try again.')

    for emp in employees:
        if emp.year >= year:
            print()
            print(emp)

if __name__ == "__main__":
    main()