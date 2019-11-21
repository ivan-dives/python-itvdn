print("число а должно быть менше b")

while True:
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    if a < b:
        s = 0
        for x in range(a, b+1):
            s += x
        print("результат = ",s)
        break
    else:
        print("ошибка, a должно быть менше b, попробуйте снова")