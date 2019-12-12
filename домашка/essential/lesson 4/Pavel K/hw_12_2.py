# Перепишите решение первого задания с помощью генератора.
def gen(t):
    for x in sorted(range (t), reverse=True):
        yield x


generator=gen(20)
for i in generator:
    print (i)