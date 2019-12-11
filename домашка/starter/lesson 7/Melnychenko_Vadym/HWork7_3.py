import random

c = int(input('Количество чисел для проверки = '))
l = random.sample(range(100), c)


def sum_l(x):
    '''Summa lista'''
    sum = 0
    for i in x:
        sum = sum + i
    return sum


def proizv_l(x):
    '''Proizvodnaya lista'''
    proizv = 1
    for i in x:
        proizv = proizv * i
    return proizv

k = 0
P_CH = []
for i in l:
    for j in range(2, i):
        if i % j == 0:
            k += 1
    if k == 0:
        P_CH.append(i)
    else:
        k = 0
print(l)
print(P_CH)
oper = int(input('''Выберите операцию:
        1 - сложение
        2 - производная
        3 - выход''' '\n'))
if oper == 1:
    print(f'Сумма простых чисел = {sum_l(P_CH)}')
elif oper == 2:
    print(f'Производная простых чисел = {proizv_l(P_CH)}')
else:
    print('Программа завершена')

