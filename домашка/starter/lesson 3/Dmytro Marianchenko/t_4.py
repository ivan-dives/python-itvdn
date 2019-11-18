import math
print("Выберите пожалуйста НОМЕР МЕНЮ необходимой операции:")
print("1. '+'","2. '-'","3. '*'","4. '/'","5. '%'","6. Площадь круга", sep="\n")
oper = input("")
if oper == "1": #сложение
    print("введите первое число:")
    x = int(input(""))
    y = int(input(""))
    print(f"Ответ: {x + y}")
elif oper == "2": #разница
    print("введите первое число:")
    x = int(input(""))
    y = int(input(""))
    print(f"Ответ: {x - y}")
elif oper == "3": #умножение
    print("введите первое число:")
    x = int(input(""))
    y = int(input(""))
    print(f"Ответ: {x * y}")
elif oper == "4": #деление
    print("введите первое число:")
    x = int(input(""))
    y = int(input(""))
    print(f"Ответ: {x / y}")
elif oper == "5":
    print("введите число от которого необходимо высчитать процент:")
    x = int(input(""))
    print("введите количество процентов в целым числом:")
    y = int(input(""))
    pers = x*(y/100)
    print(f"Ответ: {round(pers,2)}")
elif oper == "6":
    print("введите радиус:")
    r = int(input(""))
    s = math.pi*(r**2)
    print(f"Ответ: {round(s,2)}")
else:
    print(f"операция {oper}, при необходимости появится в следующей версии =)")
print("Для завершения нажмите кнопку 'Enter'...")