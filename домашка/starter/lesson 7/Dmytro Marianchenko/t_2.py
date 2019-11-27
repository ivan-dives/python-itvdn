def fib(max):
    """
    Функция выводит число Фибоначчи, согласно порядковому номеру списка.
    для работы функции, передайте число равное порядковому номеру чила Фибонначи
    """
    num1 = 0
    num2 = num1 + 1
    numbers.append(num1)
    numbers.append(num2)
    for i in range(max):
        numbers.append(numbers[-1] + numbers[-2])
        max -= 1
    del numbers[-1]
    del numbers[-2]
    return numbers

numbers = []

while True:
    max = int(input("Input a number (if you want to quit, input '00'):  "))
    if max > 0:
        fib(max)
        print(numbers[-1])
    elif max == 00:
        break

