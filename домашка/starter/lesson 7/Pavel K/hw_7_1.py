# Задание 1 Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а также сумму и среднее арифметическое его значений.

from random import randint

num = [] # create list
for i in range(20):
    num.append(randint(-10,40))

k=num[0]
sumk = 0

def minn(*args):  # min number
    global k
    for i in num:
        if i < k:
            k=i
    return(k)


def maxn(*args): # max number
    maxk = k
    for i in num:
        if i > maxk:
            maxk=i
    return(maxk)

def sumn(*args):
    global sumk
    for i in num:
        sumk += i
    return sumk


a = minn(num)
b = maxn(num)
c = sumn(num)
print(f'max number is \'{a}\', min number is \'{b}\', the sum of all numbers is {c}, average is {c/len(num)}  ')
print(num)