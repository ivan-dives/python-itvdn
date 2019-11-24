def sum(a):
    if a == b:
        return (a)
    return sum(a+1)+a


a = int(input('Введите 1-е число'))
b = int(input('Введите 2-е число'))
t = sum(a)
print(f'сумма ряда натуральных чисел между {a} и {b} ними {t}')
