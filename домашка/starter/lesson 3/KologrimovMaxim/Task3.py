a = int(input('Введите значение A: '))
b = int(input('Введите значение B: '))
c = int(input('Введите значение C: '))
print()

D = (b**2-4*a*c)

if D < 0:
    print('Отсутствуют действительные корни')
elif D == 0:
    x = -b / (2*a)
    print(f'x = {x}')
else:
    x1 = (-b + (D**0.5)) / (2*a)
    x2 = (-b - (D**0.5)) / (2*a)
    print(f'{x1 = }\n{x2 = }')
