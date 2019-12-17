def nums(var):
    try:
        result = sum(var) / len(var)
        return result
    except ZeroDivisionError:
        result = 0
        return result


lst = []
while True:
    try:
        x = int(input("Input number or input '0' to done:\n>>  "))
        if x == 0:
            break
        else:
            lst.append(x)
    except ValueError:
        print("not number")
lst_to_tup = tuple(lst)
print(*lst_to_tup)
ar = nums(lst_to_tup)
print(f"Result = {ar}")
while True:
    try:
        start = int(input("Input start point of numbers diapason:\n>>  "))
        if start <= 0:
            print("'Start' is out of range...")
            pass
        elif start >= len(lst_to_tup):
            print("'Start' is out of range...")
            pass
        else:
            start -= 1
            break
    except ValueError:
        print("not a number")
while True:
    try:
        end = int(input("Input end point of numbers diapason:\n>>  "))
        if end < start < 0:
            print("'End' is out of range...")
            pass
        elif end > len(lst_to_tup):
            print("'End' is out of range...")
            pass
        else:
            break
    except ValueError:
        print("not a number")
lst_user = lst[start:end]
lst_user = tuple(lst_user)
print(*lst_user)
ar = nums(lst_user)
print(f"Result = {ar}")
print(*lst)
while True:
    try:
        num1 = int(input("Select list number:\n>>  "))
        if num1 == 0:
            print("first number is out of range...")
            pass
        elif num1 >= len(lst_to_tup):
            print("first number is out of range...")
            pass
        else:
            num1 -= 1
            break
    except ValueError:
        print("not a number")
while True:
    try:
        num2 = int(input("Select list number:\n>>  "))
        if num2 == num1:
            print(num1 / 2)
            break
        elif num1 >= len(lst_to_tup):
            print("second number is out of range...")
            pass
        elif num2 == 0:
            print("second number is out of range...")
        else:
            num2 -= 1
            break
    except ValueError:
        print("not a number")
tmp = (num1, num2)
ar = nums(tmp)
print(f"Result = {ar}")
