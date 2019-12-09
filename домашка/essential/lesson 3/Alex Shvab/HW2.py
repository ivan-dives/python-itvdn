import datetime

COMPANY_CREATION = 2000


class Worker:
    def __init__(self, first_name, last_name, position, start_work):
        if not first_name:
            raise ValueError("Incorrect first name")
        if not last_name:
            raise ValueError("Incorrect last name")
        if not position:
            raise ValueError("Incorrect position")
        if not check_year(start_work):
            raise ValueError("Year is out of range")

        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.start_work = start_work

    def __repr__(self):
        return f"Worker: {self.first_name} {self.last_name} \n" \
               f"Position: {self.position}\nStart year: {self.start_work}"


def check_year(year):
    return COMPANY_CREATION <= year <= datetime.date.today().year


def main():
    workers = []
    while True:
        try:
            count_of_workers = int(input("Enter count of workers: "))
            break
        except ValueError:
            print("Please enter correct number")

    while len(workers) < count_of_workers:
        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            position = input("Enter position of worker: ")
            start_year = int(input("Enter year when worker start to work: "))
            worker = Worker(first_name, last_name, position, start_year)
        except ValueError as error:
            print("Error", error)
        else:
            workers.append(worker)
        finally:
            print()

    while True:
        try:
            coose_year = int(input("Enter year: "))
            break
        except ValueError:
            print("Enter correct value")

    for worker in workers:
        if worker.start_year >= coose_year:
            print(worker)


if __name__ == "__main__":
    main()
