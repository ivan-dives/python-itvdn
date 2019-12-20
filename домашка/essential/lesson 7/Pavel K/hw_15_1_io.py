from hw_15_1 import *
bd = {}
n = 0
print('|exit| If you want exit, enter "exit".\n|add| If you want add some link enter "add"\n|find|If you want find some enter "find"')


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