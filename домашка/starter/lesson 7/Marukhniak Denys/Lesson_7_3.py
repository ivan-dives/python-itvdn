# Задание 3
# Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не
# считается простым. Напишите программу, которая находит все простые числа в заданном
# промежутке, выводит их на экран, а затем по требованию пользователя выводит их сумму либо
# произведение.

print('Prime numbers start from 2nd number:')
while True:
    a = int(input('Enter start: '))
    b = int(input('Enter finish:  '))
    if a < b:
        break

num = [2, 3, 5, 7]
simple = []
result = 1

for i in range(a, b+1):
    number_is_simple = True
    for j in num:
        if i in [2, 3, 5, 7]:
            simple.append(i)
            break
        elif i in [4, 6]:
            break
        elif i % j == 0:
            number_is_simple = False
    else:
        if number_is_simple:
            simple.append(i)

print('Prime number(s):')
print(simple)
print('Do you want to use multiplication or addition on previous list of prime number(s)?')
operation = input('Enter (M) for multiplication or (A) for addition: ')

if operation.lower() == 'm':
    for i in simple:
        result *= i
    print(f'Result of multiplication: {result}')
elif operation.lower() == 'a':
    for i in simple:
        result += i
    print(f'Result of addition: {result-1}')
else:
    print('Wrong operation')
