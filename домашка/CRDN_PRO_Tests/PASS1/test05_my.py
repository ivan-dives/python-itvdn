# Створіть функцію fib_next(n) яка на вхід отримує один аргумент, що є цілим невід'ємним числом.
# Дана функція має знайти та повернути як результат наступне число в послідовності Фібоначчі, яке йде після заданого n.
# Якщо задане число n не входить у послідовність Фібоначчі, то функція має викинути (raise)
# виключення (exception) ValueError
#
# Послідовність починається з чисел (1, 2)
#
# Послідовність Фібоначчі, це така послідовність чисел, коли кожне наступне число дорівнює сумі двох попередніх.


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def fib_next(n):
    curr_i = 1
    curr_f = 1
    while curr_f < n:
        curr_i += 1
        curr_f = fibonacci(curr_i)

    if curr_f == n:
        return fibonacci(curr_i+1)
    else:
        raise ValueError


print(fib_next(1))
print(fib_next(2))
