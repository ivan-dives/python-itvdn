# Задание 2
# Перепишите решение первого задания с помощью генератора.


def generator(string):
    index = len(string)

    while True:
        index -= 1
        if index < 0:
            break
        liter = string[index]
        yield liter


string_1 = input('Enter a string: ')
print('Reversed string: ', end='')

for i in generator(string_1):
    print(i, end='')
