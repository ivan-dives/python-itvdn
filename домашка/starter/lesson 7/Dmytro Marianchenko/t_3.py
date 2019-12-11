def simple_nums(n):
    """
    проверка простых чисел в списке
    :param n:
    :return:
    """
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    s = 2
    while i * i <= n:
        if n % i == 0: return False
        i += s
        s = 6 - s
    return True

list0=[]
simple=[]
a = int(input("Введите цифру соответствующую началу вашего списка:  "))
b = int(input("Введите цифру соответствующую концу вашего списка:  "))
list0.insert(a,0)
list0 = [i for i in range(a,b+1)]
print(f"Вот ваш список {list0}")
for i in range(a, b + 1):
    if simple_nums(i):
        simple.append(i)
print(f"Вот список простых чисел из вашего списка {simple}")
summa = input(f"Если хотите получить суму этих '{simple}' простых чисел, введите 'y' или 'n' если нет:  ")
if summa == "y":
    print(f"Сумма чисел вашего списка простых чисел равна '{int(sum(simple))}'")
else:
    pass
summa_p_inpt = input(f"Если хотите получить произведение этих '{simple}' простых чисел, введите 'y' или 'n' если нет:  ")
if summa_p_inpt == "y":
    proiz = 1
    for i in range(len(simple)):
        proiz = proiz * simple[i]
    print(f"Произведение чисел вашего списка простых чисел равна '{proiz}'")