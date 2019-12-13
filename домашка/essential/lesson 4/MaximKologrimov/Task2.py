# Задание 2
# Перепишите решение первого задания с помощью генератора.

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


list = reverse([1, 2, 3, 4, 5])

for n in list:
    print(n)