# Створіть функцію find_palindromes(numbers) яка на вхід отримує список цілих невід'ємних чисел
# і на вихід повертає список чисел-паліндромів знайдених у вхідному списку.
#
# Вихідний список має бути відсортований за зростанням (менші числа спочатку) і без повторень.

def is_palindrome(n):
    sn = str(n)
    return sn == sn[::-1]


def find_palindromes(numbers):
    x_set = set([])
    for x in numbers:
        if is_palindrome(x):
            x_set |= {x}
    res_lst = list(x_set)
    res_lst.sort()
    return res_lst


print(find_palindromes([124, 121, 444, 21, 33, 44322, 956659, 9992, 33, 56743, 75357]))
