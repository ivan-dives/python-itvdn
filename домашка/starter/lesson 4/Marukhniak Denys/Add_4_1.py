from random import choice

long = int(input('Long for password: '))
amount = int(input('Amount of passwords: '))
numbers = input('Do you want to use numbers in your password(s): y/n? ')
lowercase = input('Do you want to use lowercase letters in your password(s): y/n? ')
capital = input('Do you want to use capital letters in your password(s): y/n? ')
special = input('Do you want to use special characters in your password(s): y/n? ')

symbols = ''
password = ''
numbers_all = "0123456789"
lowercase_all = "abcdefghijklmnopqrstuvwxyz"
capital_all = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_all = "@#$%{}[]\\/()'\"`~,;:.<>"

if numbers.lower() == 'y':
    symbols += numbers_all
if lowercase.lower() == 'y':
    symbols += lowercase_all
if capital.lower() == 'y':
    symbols += capital_all
if special.lower() == 'y':
    symbols += special_all

for a in range(amount):
    for l in range(long):
        password += choice(symbols)
    for index in range(long):
        if not password[index] in symbols:
            correct = 'no'
            break
    else:
        correct = 'ok'
    if correct == 'ok':
        print(f'{a+1} password is {password}')
    else:
        print(f'{a+1} password ({password}) is incorrect')
    password = ''

