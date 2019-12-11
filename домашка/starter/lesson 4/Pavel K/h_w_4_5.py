import random
t1 = '0123456789' # c 2 по 5 строку наборы символов.
t2 = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
t3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t4 = 'abcdefghijklmnopqrstuvwxyz'
list1 = []
long_pass =''
h_m_p = int(input('сколько паролей нужно'))
h_long = int(input('длина пароля'))
chto1 = input('Хотите добавить в пароль цыфры нажмите 1, нет нажмите 0')

if chto1 == '1':    # c 12 по 22 сточку спрашиваем у пользователя из каких символов будет состоять пароль
    list1.append(t1)
chto2 = input('Хотите добавить в пароль символы пунктуации нажмите 1, нет нажмите 0')
if chto2 == '1':
    list1.append(t2)
chto3 = input('Хотите добавить в пароль заглавные буквы нажмите 1, нет нажмите 0')
if chto3 == '1':
    list1.append(t3)
chto4 = input('Хотите добавить в пароль прописные буквы нажмите 1, нет нажмите 0')
if chto4 == '1':
    list1.append(t4)

for ii in range(h_m_p):

    passw = ''
    k = 0
    while k <= h_long:    # поцикловая генерация паролей
        for j in list1:
            k+=1
            t11 = random.choice(j)
            passw += t11

    passw = passw[:h_long]
    long_pass += passw + '\n'
print(long_pass)