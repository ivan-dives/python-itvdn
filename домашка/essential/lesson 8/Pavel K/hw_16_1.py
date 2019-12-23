# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
# Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.
import random
a = [random.uniform(-100000, +100000) for a in range(3)]
print(a)

with open('D:\\random.txt', 'w') as k:
    for i in a:
        k.write(str(i)+' ')

read = open('D:\\random.txt')
my_string = read.read()
my_list_str = my_string.split()
my_list_float = [float(i) for i in my_list_str]
print(sum(my_list_float))