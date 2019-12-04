#generator paroley
import random

parol = ''
pasw = ''
number = '1234567890'
z_bukv = 'ASDFGHJKLZXCVBNMQWERTYUIOP'
m_bukv = 'qwertyuiopasdfghjklzxcvbnm'
specialsim = '"@#$%{}[]\/()`~,;:.<>"'

x = int(input('Какое количество паролей сгенерировать: '))
y = int(input('Сколько символов должно быть в пароле: '))

isp_number = input('Использовать цыфры (y/n): ')
isp_m_bukv = input('Использовать прописные буквы (y/n): ')
isp_z_bukv = input('Использовать заглавные буквы (y/n): ')
isp_special = input('Использовать спец.символы (y/n): ')

if isp_special.lower() == 'y':
    pasw += specialsim
if isp_number.lower() == 'y':
    pasw += number
if isp_m_bukv.lower() == 'y':
    pasw += m_bukv
if isp_z_bukv.lower() == 'y':
    pasw += z_bukv

for i in range(x):
    parol = ''
    for j in range(y):
        parol = parol + random.choice(pasw)

    print(parol, end=('\n'))
