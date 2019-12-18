# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность
# ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.
bd = {}
n = 0
print('|exit| If you want exit, enter "exit".\n|add| If you want add some link enter "add"\n|find|If you want find some enter "find"')


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
