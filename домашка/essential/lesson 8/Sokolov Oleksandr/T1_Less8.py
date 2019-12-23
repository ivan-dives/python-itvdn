import random


lst = [random.randint(0, 10) for x in range(1000)]

with open('string.txt', 'w') as f:
    f.write(str(lst))

f = (open('string.txt', 'r'))
print(f.read())
f.close()
c = sum(lst)
print(c)