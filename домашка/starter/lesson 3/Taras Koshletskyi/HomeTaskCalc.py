import math


function = [fun for fun in dir(math) if not fun.startswith("_")]
print("In one day i will realize those functions {}".format(function))
list = ["cos", "sin", "tan"]
list2 = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponent"]
print("Please input one from list with 2 arguments {} or 1 argument {} :".format(list, list2))
choice = input("Make your choice: ")
if choice in list2:
    x = int(input("X: "))
    y = int(input("Y: "))
    if choice == "Addition":
        print(x+y)
    elif choice == "Subtraction":
        print(x-y)
    elif choice == "Multiplication":
        print(x*y)
    elif choice == "Division":
        print(x/y)
    elif choice == "Modulus":
        print(x%y)
    elif choice == "Exponent":
        print(x**y)
elif choice in list:
    x = int(input("X: "))
    method_to_call = getattr(math, choice)
    print(method_to_call(int(x)))
else:
    print("Soryan")

