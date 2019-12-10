def checker(name, year, company_bd):
    if year > company_bd:
        print(f"{name} is not an employee of the company")
    else:
        print(f"{name} works in the company since {year}")


def name_form(x):
    while x is None:
        x = input(f"Please enter:\n>> ")
        if x.isalpha():
            y = x.capitalize()
            return y
        else:
            print("should not contain a numbers")
            pass


def year_form(x):
    while x is None:
        try:
            x = int(input(f"Please enter:\n>> "))
            return x
        except ValueError:
            print("year should not contain a letter or any symbols except numbers")


def validation(x, company_bd):
    for i in x:
        if company_bd >= i[3]:
            print(f"{i[0]} {i[1]} is not а company member")
        else:
            print(f"{i[0]} {i[1]} work in {i[2]} department sins {i[3]} year")


def main():
    name = None
    surname = None
    year = None
    company_bd = 1991
    print("Enter a name of worker")
    name = name_form(name)
    print("Enter a surname of worker")
    surname = name_form(surname)
    force = input("Enter a department of company:\n>> ")
    print("Enter a year of start working in company")
    year = year_form(year)
    pers = [name, surname, force, int(year)]
    personal.append(pers)
    while True:
        sw = input("Do you wont to add an another person? y/n\n>> ")
        if sw == "y":
            break
        elif sw == "n":
            validation(personal, company_bd)
            input("Pres 'Enter' to exit...")
            exit()
    main()


if __name__ == '__main__':
    personal = []
    main()
