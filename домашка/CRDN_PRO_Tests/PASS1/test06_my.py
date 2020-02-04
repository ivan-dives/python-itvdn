# Створити функцію is_simple(n) яка на вхід отримує ціле невід'ємне число і якщо це число є простим,
# то повертає True, а якщо ні то False.
#
# Просте число  — це натуральне число, яке має рівно два різних натуральних дільники (лише 1 і саме число).


def is_simple(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True


print(is_simple(5))
