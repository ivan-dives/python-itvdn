# Задание 2
# Создайте программу, которая проверяет, является ли палиндромом введённая фраза.


def pal(string_f):
    if string_f == string_f[::-1]:
        print(f'{string_f} is a palindrome')
    else:
        print(f'{string_f} is not a palindrome')


string = input('Enter string to check it for palindrome: ')
pal(string)
