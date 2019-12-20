# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была основная часть, которая отвечала бы за
# логику работы и предоставляла обобщённый интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При замене последнего
# на другой, взаимодействующий с пользователем иным способом, программа должна продолжать корректно работать.
from hw_15_1_io import *

def add():
    print('if you want exit, enter "exit"')
    while True:
        link1 = input('enter adress')
        if link1.lower() == 'exit':
            exit()
        elif link1.lower() == 'find':
            find()
        hash1 = list(link1.split('.'))
        print(hash1)
        global n
        n += 1
        if hash1[0] == 'www':
            bd[hash1[1]] = link1
            print(f'{hash1[1]} - long link, {n} - short link')
        else:
            bd[hash1[0]] = link1
            print(f'{hash1[0]} - long link, {n} - short link')
        bd[str(n)] = link1



def find():
    print('if you want exit, enter "exit"')
    while True:
        print('Enter short or long name your link')
        enterfind = input()
        print(bd.setdefault(enterfind))
        if enterfind.lower() == 'exit':
            exit()
        elif enterfind.lower() == 'add':
            add()


while True:

    enter1 = input().lower()
    if enter1 == 'add':
        add()

    elif enter1 == 'find':
        find()

    elif enter1 == 'exit':
        exit()

    else:
        print('|exit| If you want exit, enter "exit".\n|add| If you want add some link enter "add"\n|find|If you want find some enter "find"')
