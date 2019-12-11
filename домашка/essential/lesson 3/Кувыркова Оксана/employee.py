
class Employee():
    def __init__(self):
         self.name = None
         self.surname = None
         self.department = None
         self.year_of_employment = None

    def list_of_employee(self):
        while True:
            try:
                a =[]
                quantity = int(input("how many employee"))
                for l in range(quantity):
                    b=[]
                    b.append(str(input("Name")))
                    b.append(str(input("Surname")))
                    b.append(str(input("Position")))
                    b.append(int(input("Year of employment")))
                    a.append(b)
                for employer in a:
                    for i in range(2010, 2020):
                        if i in employer:
                            print("List of employers, employed after 2010 year:")
                            print(*employer)
                        else:
                            continue
            except ValueError:
                print("You entered not valid data")

employee = Employee()
employee.list_of_employee()