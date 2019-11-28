import random

n = int(input('Количество символов в списке = '))
l = random.sample(range(1000), n)
print(l, '\n')
Z = len(l)
A, B = 0, 0

#---------------- Perebor na max i min -----------------
for i in range(Z):
    if l[i] < l[i-1]:
       A = l[i]
    if l[i] > l[i-1]:
        B = l[i]

print(f'Минимальное значение =  {A}')
print(f'Максимальное значение = {B} \n')

#---------------- S pomoshchjy vstroenyh  -----------------
print(f'Минимальное значение = {min(l)}, индекс мин числа = { l.index(min(l))}')
print(f'Максимальное значение = {max(l)}, индекс макс числа = { l.index(max(l))} \n')


def sum_l(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

print(f'Сумма всех элементов = {sum_l(l)} \n')

print(f'Среднее значение элементов списка = {sum_l(l)/n}')