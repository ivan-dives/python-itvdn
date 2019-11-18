# Самый тупой калькулятор в мире

import math

x = float(input("Enter value 1") )
z = input("Enter symbol")

if z == "cos":
    print("=", math.cos(x))
elif z == "sin":
    print("=", math.sin(x))
elif z == "tan":
    print("=", math.tan(x))
else:
    y = float(input("Enter value 2"))

    if z == "+":
        print("=",x+y)
    elif z == "-":
        print("=",x-y)
    elif z == "*":
        print("=", x*y)
    elif z == "/":
        print("=", x/y)
    elif z == "**":
        print("=", x**y)
    else:
        print("Error! unsupported operation")