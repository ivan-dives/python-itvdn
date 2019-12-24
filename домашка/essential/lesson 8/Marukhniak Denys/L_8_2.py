# Задание 2
# Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными
# файлами.
import random
import pickle


def numbs():
    return str(random.randrange(99))


lines = ''
for i in range(20):
    for j in range(25):
        lines += (numbs() + ' ').zfill(3)
    lines = (lines.rstrip() + '\n')

s = pickle.dumps(lines)
print(f'{type(s)=}     {s=}')
with open('L_8_2_b_random.bin', 'wb') as f:
    f.write(s)

with open('L_8_2_b_random.bin', 'rb') as f:
    s = f.read()

s = pickle.loads(s)
print(f'{type(s)=}     {s=}')

numbs = []
s = s.split('\n')

for i in s:
    tmp = (i.split())
    for j in tmp:
        numbs.append(j)

result = [int(x) for x in numbs]
print(f'Sum = {sum(result)}')
