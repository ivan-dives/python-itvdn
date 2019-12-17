# Задание
# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
# отсортированной в порядке возрастания.

x = input('INPUT PLZ NUMBER: ')

l = x.split(',')

l.sort(key=int)
print(l)


# list = []
#
# for x in range(5):
#     try:
#         list.append(int(input('Введите число: ')))
#     except ValueError:
#         print()
#         print('ВВЕДИТЕ ЦЕЛОЕ ЧИСЛО !!!')
#         print()
#         pass
#
# print(list)
# list.sort()
# print(list)
