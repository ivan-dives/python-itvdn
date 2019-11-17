import  math

x = int(input("Enter x: "))
PI = math.pi

if -PI <= x <= PI:
    x = x * 3
    y = math.cos(x)
    print(y)
else:
    y = x
    print(y)

