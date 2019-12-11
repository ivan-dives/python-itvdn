a = int(input("Введите значение первого числа в диапазоне_"))
b = int(input("Введите значение последнего числа в диапазоне_"))
c = []

for num in range(a, b + 1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        c.append(num)
print(c)

def Sumlist(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + Sumlist(l[1:])

def multi(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] * multi(l[1:])

q = int(input("Для получения суммы введите 1\nдля получения производного введите 2_ "))

if q == 1:
    print(Sumlist(c))
elif q == 2:
    print(multi(c))