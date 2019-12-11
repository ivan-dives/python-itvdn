print("квадратное уравнение:")
print("a*x^2 + b*x + c = 0")
a = int(input("Введите число 'а':"))
b = int(input("Введите число 'b':"))
c = int(input("Введите число 'c':"))
discr = b**2-4*a*c #Дискриминант
if (discr > 0): #два корня
    x1 = (-b+discr**0.5)/(2*a)
    x2 = (-b-discr**0.5)/(2*a)
    print("результат:")
    print(f"Дискриминант равен {discr}")
    print(f"x1= {x1}\nx2= {x2}")
elif (discr == 0): #один корень
    x = -b/(2*a)
    print(f"x= {x}")
else:
    print("нет корней")
input("для завершения нажмите 'Enter'")