print("ax^2 + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = ((b ** 2) - 4 * a * c) ** 0.5

if d < 0:
    print("No roots (")
elif d == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(f"x1 = {x1}\n x2 = {x2}")