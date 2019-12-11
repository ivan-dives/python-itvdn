MEMOIZE = [0, 1]

def fg(x):
    if len(MEMOIZE) > x:
        return MEMOIZE[x]
    else:
        s = fg(x - 1) + fg(x - 2)
        MEMOIZE.insert(x, s)
        return s

while True:
    a = int(input('Введите количество ступеней: '))
    if a <= 0:
        print("Вы ввели недопустимое значение, значение должно быть больше 0.\nПопробуйте еще раз.")
    else:
        break

print("результат -",fg(a))