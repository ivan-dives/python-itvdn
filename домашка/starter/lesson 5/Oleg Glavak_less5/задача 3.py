# Самый тупой калькулятор в мире v 2.0

def pl(x, y):
    print("=", x + y)

def min(x, y):
    print("=", x - y)

def mult(x, y):
    print("=", x * y)

def div(x, y):
    while z == "/":
        if x == 0:
            print("Errorr! It is impossible to divide by 0. Try again !!!")
        elif y == 0:
            print("Errorr! It is impossible to divide by 0. Try again !!!")
        else:
            print("=", x / y)
        break

while True:
    print("To continue, press any key. To exit, press exit.")
    stop = input("")
    if stop == "exit":
        break

    x = float(input("value 1: "))
    y = float(input("value 2: "))
    z = input("Enter +, -, *, /: ")
    if z == "+":
        pl(x, y)
    elif z == "-":
        min(x, y)
    elif z == "*":
        mult(x, y)
    elif z == "/":
        div(x, y)
    else:
        print("function not supported, try again")