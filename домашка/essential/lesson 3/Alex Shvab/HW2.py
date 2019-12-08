import datetime



class Worker:
    def __init__(self, first_name, last_name, position, start_job):
        if not first_name:
            raise ValueError("Incorrect first name")
        if not last_name:
            raise ValueError("Incorrect last name")
        if not position:
            raise ValueError("Incorrect position")
        if not check_year(start_job):
            raise ValueError("Year is out of range")


def check_year(year):
    return