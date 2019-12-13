# Задание
# Напишите функцию-генератор для получения n первых простых чисел.


def prime(n):
   d = 2
   if n == 1:
       n = False
   while n % d != 0:
       d += 1
   return d == n

def list_prime():
    list = []
    for y in range(1, 9999):
        if prime(y) == True:
            list.append(y)
            x = len(list)
            if x < z:
                yield list
            if x == z:
                yield list


z = int(input("Введите знанчение: "))

l = list_prime()

for i in l:
    print(i)


# try:
#     print(next(l))
#     print(next(l))
#     print(next(l))
#     print(next(l))
#     print(next(l))
# except:
#     pass