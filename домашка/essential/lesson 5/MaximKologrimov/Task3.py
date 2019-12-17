# Задание 3
# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
# данного текста.

x = input('INPUT PLZ TEXT: ')

list = x.split(',')
print(list)

list.sort(key=str)
print(list)