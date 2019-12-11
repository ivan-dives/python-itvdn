import sys

for i in range(3):
    for j in range(4):
        print('*', end='')
    print()

# новая версия

sys.exit()

for x in []:
    print(10)

sys.exit()

x = 2
stop = 10
step = 2

while x < stop:
    print(x)
    x += step

sys.exit()

#for x in range(2, 10, 2):
#    print(x)

sys.exit()

#import pprint
#pprint.pprint('hi')

#ftp = ftplib.FTP()


#passw = input('введите пароль')

LOGIN = 'ivan'
PASSWORD = '5'
TRIES = 3

passw = '10'

while True:
    l = input('введите логин: ')

    if l != LOGIN:
        print('логин неправильный')
        continue

    print('логин правильный')
    for x in range(TRIES):
        p = input(f'введите пароль (попытка {x+1}): ')
        if p != PASSWORD:
            print('неправильный пароль')
            continue
        else:
            break # вот здесь выходит for
    else:
        continue # вот здесь продолжается while
    print('before break')
    break # вот здесь выходит while

sys.exit(0)

# выходим когда условие цикла False -> выполняется блок если
# выходим по оператору break

#passw = input('введите пароль')



#while passw != PASSWORD:
#    passw = input('неправильный пароль, введите пароль')
#else:
#    print('правильный пароль')

#while True:
#    if expr is False:
#        break
#    else:
#        continue

# выходим когда закончилась коллекция -> выполняется блок если
# выходим по оператору break

#for x in range(3):
#    #print(x)
#    passw = input(f'введите пароль (попытка {x+1}): ')
#    if passw != PASSWORD:
#        continue

#    print('правильный пароль')
#else:
#    print('стойте на месте, за вами выехали')
#    import sys
#    sys.exit(1)

#print('добро пожаловать в нашу защищенную компанию')
#print('правильный пароль')

LOGIN = 'ivan'
PASSWORD = '5'

while True:
    s = input('введите логин и пароль через пробел: ')
    l, p = s.split(' ')

    if l != LOGIN:
        print('неправильный логин')
        continue

    if p != PASSWORD:
        print('неправильный пароль')
        continue

    print('добро пожаловать')
    break
