#!/usr/bin/python3
# -*- coding: utf-8 -*_

import random

str1 = '0123456789'
str2 = 'abcdefghijklmnopqrstuvwxyz'
str_optional = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

def check_inputs(length, count):
    """
    This function check inputs length for passwords
    and counts to generate number of passwords
    """
    return length >= 6 and count >= 1


def check_symbols(choice):
    """
    check if user input YES otherway -> False
    """
    choice_bool = False
    if choice.lower() == "y" or choice.lower() == "yes":
        choice_bool = True
    return choice_bool


def password(length, choice):
    """
    If all ok - generate passwords
    """
    password = ""
    x = 3
    if choice:
        x = 4
    for i in range(length):
        use_symbol = random.randint(1, x)
        if use_symbol == 1:
            password += str1[random.randint(0, len(str1)-1)]
        elif use_symbol == 2:
            password += str2[random.randint(0, len(str2)-1)].upper()
        elif use_symbol == 3:
            password += str2[random.randint(0, len(str2)-1)]
        elif use_symbol == 4:
            password += str_optional[random.randint(0, len(str_optional)-1)]
    return password


def pass_generator(length, count, choice):
    """
    If all ok - generate passwords
    """
    if check_inputs(length, count):
        return [password(length, choice) for i in range(count)]
    return ""


def main():
    while True:
        length = int(input("Please input length of password min 6: "))
        count = int(input("Please input number of passwords min 1: "))
        choice = input("Do you want symbols Y/N: ")
        lst = pass_generator(length, count, check_symbols(choice))
        if lst:
            print(lst)
            break
        else:
            print("Plese insert correct data")


if __name__ == '__main__':
    main()
