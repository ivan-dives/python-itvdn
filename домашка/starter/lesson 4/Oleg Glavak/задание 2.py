print("n > 0")

while True:
    n = int(input("Введите число n: "))
    if n > 0:
        s=1
        for x in range(2, n+1):
            s *= x
        print("результат = ", s)
        break
    else:
        print("ошибка, значение n должно быть больше 0, попробуйте снова")