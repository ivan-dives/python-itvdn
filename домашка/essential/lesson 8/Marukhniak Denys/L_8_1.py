# Задание 1
# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
# действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
# сумму.
import random


def numbs():
    return str(random.randrange(99))


with open('L_8_1_random.txt', 'w') as f:
    for i in range(20):
        line = ''
        for j in range(25):
            line += (numbs() + ' ').zfill(3)
        f.write(line.rstrip() + '\n')

with open('L_8_1_random.txt', 'r') as f:
    s = f.read()

print(type(s))
numbs = []
s = s.split('\n')

for i in s:
    tmp = (i.split())
    for j in tmp:
        numbs.append(j)

result = [int(x) for x in numbs]
print(f'Sum = {sum(result)}')
