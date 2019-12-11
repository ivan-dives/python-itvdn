def hanb(n, a, b, c):
    if (n == 0):
        return

    else:
        hanb(n - 1, a, c, b)
        print(a, b)
        hanb(n - 1, c, b, a)


n = int(input('Введите высоту башни: '))

hanb(n, 1, 2, 3)