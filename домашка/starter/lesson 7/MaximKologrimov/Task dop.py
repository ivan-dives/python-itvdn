# Задание
# Создайте список, введите количество его элементов и сами значения, выведите эти значения на
# экран в обратном порядке.

from random import randint
list = [randint(1, 100) for x in range(10)]

num = 0
for x in list:
    num = num + 1
    print(f'{num} >> {x}')

print()
print(f'Кол-во элементов: {len(list)}')

print(f'Сами элементы: {list}')

print(f'Перевернутый список: {list[::-1]}')