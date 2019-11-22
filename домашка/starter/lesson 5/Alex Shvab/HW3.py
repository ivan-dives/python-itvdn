def add(x, y):
    sum = x + y
    print(f"{x} + {y} = {sum}")

def sub(x, y):
    sum = x - y
    print(f"{x} - {y} = {sum}")

def mul(x, y):
    sum = x * y
    print(f"{x} * {y} = {sum}")

def div(x, y):
    if y == 0:
        print("Error: Can not division by zero")
    else:
        sum = x / y
        print(f"{x} / {y} = {sum}")

while True:
    print("""Choose an operation:
    1. Adding
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit""")

    choose = int(input(">"))

    if choose == 1:
        x = int(input("Enter first operand: "))
        y = int(input("Enter second operand: "))
        add(x, y)
    elif choose == 2:
        x = int(input("Enter first operand: "))
        y = int(input("Enter second operand: "))
        sub(x, y)
    elif choose == 3:
        x = int(input("Enter first operand: "))
        y = int(input("Enter second operand: "))
        mul(x, y)
    elif choose == 4:
        x = int(input("Enter first operand: "))
        y = int(input("Enter second operand: "))
        div(x, y)
    elif choose == 5:
        print("Exit")
        break
    else:
        print("Incorect")

