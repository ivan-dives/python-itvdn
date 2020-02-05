# Створіть функцію find_palindromes(numbers) яка на вхід отримує список цілих невід'ємних чисел
# і на вихід повертає список чисел-паліндромів знайдених у вхідному списку.
#
# Вихідний список має бути відсортований за зростанням (менші числа спочатку) і без повторень.


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_palindromes(numbers):
    return sorted(
        set(
            num for num in numbers if is_palindrome(num)
        )
    )


print(find_palindromes([124, 121, 444, 21, 33, 44322, 956659, 9992, 33, 56743, 75357]))