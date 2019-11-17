import math

action = input("action: ")
result = None
x = float(input("x = "))
if action is "sin" or "cos" or "tan":
    if action == "cos":
        result = math.cos(x)
    elif action == "sin":
        result = math.sin(x)
    elif action == "tan":
        result = math.tan(x)
else:
    y = float(input("y = "))
    if action == "+":
        result = x + y
    elif action == "-":
        result = x - y
    elif action == "*":
        result = x * y
    elif action == "/":
        result = x / y
    elif action == "pw":
        result = x**y


print(result)