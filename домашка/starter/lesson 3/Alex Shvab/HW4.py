import  math

oper = """Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Sin
7. Cos
8. Tan\n"""
print(oper)

choise = int(input("Choose operation: "))

if choise == 1:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    x = a + b
    print(x)
elif choise == 2:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    x = a - b
    print(x)
elif choise == 3:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    x = a * b
    print(x)
elif choise == 4:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    x = a / b
    print(x)
elif choise == 5:
    a = int(input("Enter operand: "))
    b = int(input("Enter power: "))
    x = a ** b
    print(x)
elif choise == 6:
    a = int(input("Enter a: "))
    x = math.sin(a)
    print(f"Sin(x) = {x}")
elif choise == 7:
    a = int(input("Enter a: "))
    x = math.cos(a)
    print(f"Cos(x) = {x}")
elif choise == 8:
    a = int(input("Enter a: "))
    x = math.tan(a)
    print(f"Tan(x) = {x}")
else:
    print("You shall not pass")