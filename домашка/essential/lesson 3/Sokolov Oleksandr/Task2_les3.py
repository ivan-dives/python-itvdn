def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
  try:
      return a / b
  except ZeroDivisionError:
      print("Divide by 0 Error")

def pow(a, b):
    try:
        return a ** b
    except ZeroDivisionError:
        print("Raising to the power of a negative number")

if __name__ == "__main__":
    operator_map = {"+": add, "-": sub, "*": mul, "/": div, "pow": pow}

    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("That is not a number!")
            continue

        operator = input("Enter an operator (valid operators are +, -, *, / and pow): ")
        print(operator_map[operator](number1, number2) if operator in operator_map else "Invalid operator!")