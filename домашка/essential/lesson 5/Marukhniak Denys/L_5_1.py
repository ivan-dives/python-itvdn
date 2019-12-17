# Задание 1
# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
# арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
# чисел и среднее арифметическое чисел из заданного диапазона.


def avg(*args):
    return sum(args)/len(args)


numbs = input('Enter numbers: ')
numbs = numbs.split()
numbs = [int(i) for i in numbs]
print('Average of', numbs, '= ', end='')
print(avg(*numbs))
