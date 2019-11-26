# Задание 2
# Создайте программу, которая проверяет, является ли палиндромом введённая фраза.

word = input('Введите палиндром: ')

def palindrom(word):
    word = word[::-1]
    return word

if word == palindrom(word):
    print('Это палиндром,', word == palindrom(word))
else:
    print('Это не палиндром,', word != palindrom(word))