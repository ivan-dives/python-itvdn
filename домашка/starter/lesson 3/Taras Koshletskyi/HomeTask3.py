import math


def check_name(name, my_name="Taras"):
    return name[0:].lower() == my_name[0:].lower()


def fun_y(number):
    if -math.pi <= number <= math.pi:
        print("y = cos(3x) = ", end="")
        return math.cos(3 * number)
    print("y = x = ", end="")
    return number


name_input = input("Hello, Could you plese insert your name: ")
print("Damn, I have the same name" if check_name(name_input) else "Sorry, bad answer bro")


x = None
while True:
    x = input("Input x: ")
    if x.startswith("-") and x[1:].isdigit() or x.isdigit():
        x = int(x)
        print("Molodec\'")
        break
    print("Try again")

print(fun_y(x))


print("Input datas (ax^2 + bx + c = 0): ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Discriminant D = {0:.2f}".format(discr))
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("No roots")
