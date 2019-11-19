import math

x1 = input("Введите первый аргумент x1 = ")
operation_name = input("Введите имя операции (+, -, *, /, ^, sin, cos, tg):")
need2operand = (operation_name == "+") or (operation_name == "-") or (operation_name == "*") \
               or (operation_name == "/") or (operation_name =="^")
if need2operand:
    x2 = input("Введите второй аргумент x2 = ")

if operation_name == "+":
    res = float(x1)+float(x2)
    print("x1 + x2 = {}".format(res))
elif operation_name == "-":
    res = float(x1) - float(x2)
    print("x1 - x2 = {}".format(res))
elif operation_name == "*":
    res = float(x1) * float(x2)
    print("x1 * x2 = {}".format(res))
elif operation_name == "/":
    res = float(x1) / float(x2)
    print("x1 / x2 = {}".format(res))
elif operation_name == "^":
    res = float(x1) ** float(x2)
    print("x1 ^ x2 = {}".format(res))
elif operation_name == "sin":
    res = math.sin(float(x1))
    print("sin(x1) = {}".format(res))
elif operation_name == "cos":
    res = math.cos(float(x1))
    print("cos(x1) = {}".format(res))
elif operation_name == "tg":
    res = math.tan(float(x1))
    print("tg(x1) = {}".format(res))
else:
    print("Некоректное имя операции!")