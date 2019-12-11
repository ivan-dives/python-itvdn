import operator

def enter_operation():
    operation = input("Choose operation (+, -, *, /, ^) or type exit :")
    if operation == "+":
        return operator.add
    elif operation == "-":
        return operator.sub
    elif operation == "*":
        return operator.mul
    elif operation == "/":
        return  operator.truediv
    elif operation == "^":
        return operator.pow
    elif operation == "exit":
        exit()
    else:
        raise NotImplementedError("Incorrect operation")


def main():
    while True:
        try:
            operation = enter_operation()
            a = int(input("Enter first operand: "))
            b = int(input("Enter second operand: "))
            result = operation(a, b)
        except ZeroDivisionError:
            print("Please don't divide by zero")
        except ValueError:
            print("Please use only numbers")
        else:
            print(f"{result=}")
        finally:
            print()


if __name__ == '__main__':
    main()