# Задание
# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые
# входят в заданный промежуток.

x = int(input('Введите натуральное число №1: '))
y = int(input('Введите натуральное число №2: '))

def sum(a, b):
    def minimal(a, b):
        rmin = min(a, b)
        return rmin
    def maximal(a, b):
        rmax = max(a, b)
        return rmax
    if a == b:
        return a
    else:
        return maximal(a, b) + sum(minimal(a, b), maximal(a, b) -1)


print('Сумма натуральных чисел: ', sum(x, y))