# Даны две строки. Выведите на экран символы, которые есть в обоих строках.
string1= set(input('Put your string'))
string2= set(input('Put new string'))
print(string1.intersection(string2))