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

class MyError(ValueError, ArithmeticError):
    def __init__(self):
        Exception.__init__(self, "well, that rather badly didnt it?")


def main():
    while True:
        try:
            operation = enter_operation()
            a = int(input("Enter first operand: "))
            b = int(input("Enter second operand: "))
            result = operation(a, b)
            break
        except MyError as e:
            print(f"LOH")

if __name__ == '__main__':
    main()