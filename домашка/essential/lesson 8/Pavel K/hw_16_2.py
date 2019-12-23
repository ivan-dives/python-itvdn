# Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными файлами.
import random
a = [random.uniform(-100000, +100000) for a in range(10000)]
print(a)
with open('D:\\random.dat', 'wb') as k: #меняем расширение файла на dat и ставим флаг 'b'
    for i in a:
        k.write(bytes(str(i)+' ', 'utf8')) # преобразовываем в строку и в байты и указываем кодировку.


read = open('D:\\random.dat')
my_string = read.read()
my_list_str = my_string.split()
my_list_float = [float(i) for i in my_list_str]

print(sum(my_list_float))