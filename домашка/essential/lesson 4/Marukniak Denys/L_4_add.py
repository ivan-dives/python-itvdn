# Задание
# Напишите функцию-генератор для получения n первых простых чисел.

print('Prime numbers start from 2nd number:')
while True:
    a = 2
    b_end = int(input('How many prime numbers should be displayed? '))
    if a < b_end:
        break


def prime_number(b):
    num = [2, 3, 5, 7]
    i = 2
    while True:
        number_is_simple = True
        for j in num:
            if i in [2, 3, 5, 7]:
                b -= 1
                yield i
                break
            elif i in [4, 6]:
                break
            elif i % j == 0:
                number_is_simple = False
        else:
            if number_is_simple:
                b -= 1
                yield i
        i += 1
        if b == 0:
            break


print('Prime number(s):')

for x in prime_number(b_end):
    print(x, end=' ')
