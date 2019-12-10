def operations(a, b):
    operation = input("What operation do you need:\n1. If add enter '+' \n2. If subtract enter '-' \n3. If "
                      "multiplication enter '*' \n4. If division enter '/'\n5. If exponentiation enter '^' \n>>  ")
    if operation == "+":
        r = a + b
        return r
    elif operation == "-":
        r = a - b
        return r
    elif operation == "*":
        r = a * b
        return r
    elif operation == "/":
        try:
            r = a / b
            return r
        except ZeroDivisionError:
            r = "no result"
            return r
    elif operation == "^":
        try:
            r = a ** b
            return r
        except ZeroDivisionError:
            r = "no result"
            return r
    else:
        print("Wrong operation choice... try again")
        operations(a, b)


def inp_nums(x):
    while x is None:
        try:
            x = float(input("enter a number:\n>> "))
        except ValueError:
            print("It is not a number... try again")
    return x


def main():
    num1 = None
    num2 = None
    num1 = inp_nums(num1)
    print("and second number")
    num2 = inp_nums(num2)
    result = operations(num1, num2)
    result_end = result % 1
    if result_end == 0:
        print(round(result))
    else:
        print(result)
    to_do = input("If you want to continue press 'Enter' or input 'exit':\n>> ")
    if to_do == exit:
        exit()
    else:
        main()


if __name__ == '__main__':
    main()
