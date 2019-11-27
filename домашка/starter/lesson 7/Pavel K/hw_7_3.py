n = int(input('До какого числа нужно взять простые числа?'))
a = list(range(n))
t = []
k = 0

for i in range(n):
    if i % 2 != 0 and i % 3 != 0:
        t.append(i)
        k += i

print(t)

print('Вывести сумму чисел нажми 1')
sumn = int(input())
if sumn == 1:
    print(k)
else:
    exit(0)
