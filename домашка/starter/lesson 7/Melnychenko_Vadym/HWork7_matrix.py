import random

l = [
    random.sample(range(10), 4),
    random.sample(range(10), 4),
    random.sample(range(10), 4)
    ]
print('Входная матрица:', *l, sep='\n')
print('\n')
l2 = [list(a) for a in list(zip(*l))]

print('Транспонированная матрица:', *l2, sep='\n')
print('\n')

#---------------------Umnogenie matric----------------------------
sm = 0
t = []
l3 = []
if len(l) != len(l2[0]):
    print("Матрицы не одинаковыe")
else:
    sr = len(l)
    sb = len(l[0])
    sb2 = len(l2[0])
    for z in range(0, sr):
        for j in range(0, sb2):
            for i in range(0, sb):
                sm = sm + l[z][i] * l2[i][j]
            t.append(sm)
            sm = 0
        l3.append(t)
        t = []
print('Mатрица 3:', *l3, sep='\n')