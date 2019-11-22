#  Создайте две функции, вычисляющие значения определённых алгебраических выражений.
#  Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

# Функция, возвращающя переданный аргумент, возведённый в квадрат
def square(x):
    return x*x


# Функция, возвращающя переданный аргумент, возведённый в куб
def cube(x):
    return x*x*x

# Цикл на экран таблицы значений этих функций от -5 до 5 с шагом 0.5.
a = -5
while a <= 5:
    if a < - 3:
        print("x={},    x^2={},     x^3={}".format(a, square(a), cube(a)))
        print("x={},  x^2={},  x^3={}".format(a + 0.5, square(a + 0.5), cube(a + 0.5)))
    elif a < 0:
        print("x={},    x^2={},      x^3={}".format(a, square(a), cube(a)))
        print("x={},  x^2={},   x^3={}".format(a + 0.5, square(a + 0.5), cube(a + 0.5)))
    elif a <= 3:
        print("x={},     x^2={},      x^3={}".format(a, square(a), cube(a)))
        if a < 3:
            print("x={},   x^2={},   x^3={}".format(a + 0.5, square(a + 0.5), cube(a + 0.5)))
        else:
            print("x={},   x^2={},  x^3={}".format(a + 0.5, square(a + 0.5), cube(a + 0.5)))
    else:
        print("x={},     x^2={},     x^3={}".format(a, square(a), cube(a)))
        print("x={},   x^2={},  x^3={}".format(a + 0.5, square(a + 0.5), cube(a + 0.5)))
    a += 1

