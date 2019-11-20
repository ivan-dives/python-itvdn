import random

long = int(input('Long for password: '))
amount = int(input('Amount of passwords: '))
numbers = input('Do you want to use numbers in your password(s): y/n? ')
lowercase = input('Do you want to use lowercase letters in your password(s): y/n? ')
capital = input('Do you want to use capital letters in your password(s): y/n? ')
special = input('Do you want to use special characters in your password(s): y/n? ')
num = numbers.lower()
low = lowercase.lower()
cap = capital.lower()
sp = special.lower()

symbols = ''
password = ''
numbers_all = "0123456789"
lowercase_all = "abcdefghijklmnopqrstuvwxyz"
capital_all = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_all = "@#$%{}[]\\/()'\"`~,;:.<>"

for a in range(amount):
    for l in range(long):
        if num == 'y':
            symbols += numbers_all
        if low == 'y':
            symbols += lowercase_all
        if cap == 'y':
            symbols += capital_all
        if sp == 'y':
            symbols += special_all
        password += random.choice(symbols)
    for index in range(long):
        if not password[index] in symbols:
            print('How does it possible?')
    print(f'{a+1} password is {password}')
    password = ''
