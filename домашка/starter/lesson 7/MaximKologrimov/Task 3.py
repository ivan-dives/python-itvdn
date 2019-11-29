# Задание 3
# Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не
# считается простым. Напишите программу, которая находит все простые числа в заданном
# промежутке, выводит их на экран, а затем по требованию пользователя выводит их сумму либо
# произведение.

def prime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

def sumlist(none):
    sum = 0
    for x in none:
        sum = sum + int(x)
    return sum

def multlist(none):
    mult = 1
    for x in none:
        mult = mult * int(x)
    return mult

#d = int(input('Введите длинну списка: '))

a = int(input('Список начинается с: '))
b = int(input('Список заканчивается на: '))

if a < b:
    list = [(x) for x in range(a, b+1)]
    print(list)
else:
    print('Ошибка, "a" должно быть меньше "b" !!!')

print()


list2 = []
for y in range(a, b):
    if prime(y) == True:
        list2.append(y)
else:
    print(list2)

print()

print('''Сумма или Произведение?
    1. Сумма
    2. Произведение
    3. Выход
''')

choice = input('Сделайте выбор: ')
if choice == '1':
    print(sumlist(list2))
elif choice == '2':
    print(multlist(list2))
elif choice == '3':
    print('Exit')
else:
    print('Error')
