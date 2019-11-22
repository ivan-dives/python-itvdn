#Задание 3
#Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на
#экран прямоугольный треугольник.

for n in range(6):
    for m in range(n):
        print('*', end='')
        print(' ', end='')
    print()