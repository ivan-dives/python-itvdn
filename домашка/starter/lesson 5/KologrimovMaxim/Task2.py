# Задание 2
# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

x = int(input('Введите значение: '))
y = int(input('Введите значение: '))
print()

if x < 999 and y < 999 and x > -999 and y > -999:
    def exp1(a, b):
        if a > -5:
            a += 5
        if b > -5:
            b += 5
        c = a * b
        if c > 0:
            c = -1*c
        c = int(c)
        #print('Значение всегда < -5: ', c)

        while c !=-0.5:
            c += 0.5
            if c >= -5:
                print(f'* Значение функции № 1 * {c} *')
                print('*******************************')

    def exp2(a, b):
        if a < 5:
            a += 5
        if b < 5:
            b+= 5
        c = a + b
        if c > 0:
            c = -1*c
        c = int(c)
        #print('Значение всегда < -5:  ', c)

        while c != 5:
            c = c + 0.5
            if c > -0.5:
                print(f'* Значение функции №2 *   {c} *')
                print('*******************************')

    print('*******************************')
    exp1(x, y)
    exp2(x, y)
else:
    print('В следующий раз вводите значение от -999 до 999')