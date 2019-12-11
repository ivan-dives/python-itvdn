# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

def err(x):
    try:
        x / 0
    except ZeroDivisionError:
        print('Ошибка ZeroDivisionError')
        raise
try:
    z = int(input('Введите значение: '))
    err(z)
except ValueError:
    print('Ошибка ValueError')
    raise