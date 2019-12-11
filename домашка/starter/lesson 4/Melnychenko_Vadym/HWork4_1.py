print('Соблюдайте условие  A < B')
a = int(input('Введите число A: '))

b = int(input('Введите число B: '))

s = a

if a > b:
    print('''Условие не было соблюдено!
Я не буду ничего считать!!!''')

else:
    while a < b:
        a = a + 1
        s = s + a
    else:
        print(s)