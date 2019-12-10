class Worker_Error(Exception):
    pass
class Data_Error(Worker_Error):
    pass
class Name_Error(Data_Error):
    pass
class Department_Error(Data_Error):
    pass
class Year_Error(Data_Error):
    pass


est = 1989
year = 2019


class Worker:
    def __init__(self, n=None, nn=None, d=None, y=None):
        if len(n) < 2 or not n.isalpha():
            raise Name_Error('Fist Name Error')
        if len(nn) < 2 or not nn.isalpha():
            raise Name_Error('Last Name Error')
        if len(d) < 2 or not d.isalpha():
            raise Department_Error('Department Error')
        if not y.isdigit():
            raise Year_Error('Year Error')
        else:
            y = int(y)
            if est > y or y > year:
                raise Year_Error('Year Error')
            else:
                self.n = n
                self.nn = nn
                self.d = d
                self.y = y

    def __str__(self):
        return f'{self.n} {self.nn} ({self.d} Dept.) - employed since {self.y}'


w1 = None
w2 = None
w3 = None
w4 = None
w5 = None
w6 = None
workers = [w1, w2, w3, w4, w5, w6]
i = 0
while i < len(workers):
    print(f'Enter data for employee #{i + 1}:')
    v1 = input('First Name: ')
    v2 = input('Last Name: ')
    v3 = input('Department: ')
    v4 = input('Employed since (year): ')
    try:
        workers[i] = Worker(v1, v2, v3, v4)
        i += 1
    except Name_Error as ne:
        print(f'{ne}: Employee name can only contain letters\n'
              'and must be at least two characters long')
    except Department_Error as de:
        print(f'{de}: Department name can only contain letters\n'
              'and must be at least two characters long')
    except Year_Error as ye:
        print(f'{ye}: Year must be entered in four-digit format\n'
              f'and be within {est} - {year}')

print()
print(*workers, sep='\n')
