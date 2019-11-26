# Задание 2
# Создайте программу, которая проверяет, является ли палиндромом введённая фраза.


def rev_str1(phrase):
    """
    Первая функция реверса строки
    :param phrase: реверсируемая строка
    :return: реверснутая строка
    """
    rev_str = phrase[::-1]
    return rev_str


def rev_str2(phrase):
    """
    Вторая функция реверса строки
    :param phrase: реверсируемая строка
    :return: реверснутая строка
    """
    rev_str = "".join(reversed(phrase))
    return rev_str


def is_palindrome(str_tst, func_rev):
    return str_tst == func_rev(str_tst)


inp_str = input("Введите фразу: ")
print("Тест1: это палиндром") if is_palindrome(inp_str, rev_str1) else print("Тест1: это НЕ палиндром")
print("Тест2: это палиндром") if is_palindrome(inp_str, rev_str2) else print("Тест2: это НЕ палиндром")
