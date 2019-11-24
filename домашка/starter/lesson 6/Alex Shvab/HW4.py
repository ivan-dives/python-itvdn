def range(a, b):
    "Выставляем введеные значения в нужном порядке"
    start = min(a, b)
    end = max(a, b)
    def sum (s , e):
        "Рекурсивно сумируем все значения в заданом диапазоне"
        if e == s:
            return s
        else:
            return e + sum(s, e-1)
    print(sum(start, end))


x = int(input("Enter x: "))
y = int(input("Enter y: "))
range(x, y)