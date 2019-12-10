
def calculate(x, y):

    action = input("choose a nesessary operation: +, -, /, ^ - ")
    if action == "+":
        result = x + y
        return result
    elif action == "-":
        result = x - y
        return result
    elif action == "/":
        try:
            result = x / y
            return result
        except ZeroDivisionError as exception:
            print("it is impossible to divide by zero")
            result = None
            return result
    elif action == "*":
        result = x * y
    elif action == "^":
        try:
            result = x ** y
            return result
        except ArithmeticError as exception:
            print()
    

def main():
    while True:
        try:
          x = float(input("x = "))
          y = float(input("y = "))
          result = calculate(x, y)
          print(result)
        except ValueError as exception:
            print("enter correct data")
        finally:
            print()

       
if __name__ == '__main__':
    main()
