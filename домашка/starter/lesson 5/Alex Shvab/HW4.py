def average(a, b, c):
    res = (a + b + c) / 3
    print(res)

while True:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    c = int (input("Enter third operand: "))
    average(a, b, c)


    exit = input("Do you wont exit y / n : ")
    if exit == "y":
        break
    else:
        continue