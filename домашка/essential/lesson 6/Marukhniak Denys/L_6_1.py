# Задание 1
# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

# print(f'{str1}\n{str2}')
s_chr = set(str1) & set(str2)
print('Same chars in both strings: ', end='')
print(*s_chr, sep=', ')
