import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b ** 2 - 4 * a *c

print(D)

if D < 0:
    print("There are no valid results")

if D == 0:
    x = -b / (2 * a)
    print(x)

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    
    print(x1)
    print(x2)
    
