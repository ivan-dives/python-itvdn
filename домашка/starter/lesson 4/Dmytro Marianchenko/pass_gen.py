print("Генератор паролей")

lenght_p = int(input("Какой длинны хотите пароль? Введите цифрой длинну пароля:  "))
while lenght_p < 1:
    lenght_p = int(input("Какой длинны хотите пароль? Введите цифрой длинну пароля:  "))
lenght_sum = 0


l_case = input("Вы хотите использовать в пароле латинские символы нижнего регистра? y = Да, n = Нет?:  ")
l_case_count = 0
p_l_case = 0
while True:
    if l_case == "y":
        l_case_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
        while l_case_count > lenght_p:
            print("недостаточное количество определенных ранее символов!!!")
            l_case_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
        lenght_sum = lenght_p - l_case_count
        if lenght_sum == 0:
            print("Все зарезервированные символы использованы")
        elif lenght_sum != 0:
            print(f"Отлично, еще осталось определить {lenght_sum} символ(ов)")
        break
    elif l_case == "n":
        break
    else:
        print(f"вы ввели '{l_case}', считаем что это 'нет'... поехали дальше")
        break

u_case_count = 0
p_u_case = 0
if lenght_sum != 0:
    u_case = input("Вы хотите использовать в пароле латинские символы верхнего регистра? y = Да, n = Нет?:  ")
    u_case_count = 0
    while True:
        if u_case == "y":
            u_case_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
            while u_case_count > lenght_sum:
                print("Выше предельного количество определенных ранее символов!!!")
                u_case_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
            lenght_sum = lenght_sum - u_case_count
            if lenght_sum == 0:
                print("Все зарезервированные символы использованы")
            elif lenght_sum != 0:
                print(f"Отлично, еще осталось определить {lenght_sum} символ(ов)")
            break
        elif u_case == "n":
            break
        else:
            print(f"вы ввели '{u_case}', считаем что это 'нет'... поехали дальше")
            break
else:
    pass

numbers_count = 0
p_num_case = 0
if lenght_sum != 0:
    numbers = input("Вы хотите использовать в пароле цифры? y = Да, n = Нет?:  ")
    while True:
        if numbers == "y":
            numbers_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
            while numbers_count > lenght_sum:
                print("Выше предельного количество определенных ранее символов!!!")
                numbers_count = int(input("Веедите количество сомволов которое вы хотите использовать?:  "))
            lenght_sum = lenght_sum - numbers_count
            if lenght_sum == 0:
                print("Все зарезервированные символы использованы")
            elif lenght_sum != 0:
                print(f"Отлично, еще осталось определить {lenght_sum} символ(ов)")
            break
        elif numbers == "n":
            numbers_count = 0
            break
        else:
            numbers_count = 0
            print(f"вы ввели '{numbers}', считаем что это 'нет'... поехали дальше")
            break
else:
    pass

if lenght_sum > 0:
    print(f"Остаток {lenght_sum} неназначенных символов от общей длинны пароля будет назначено рандомно")
else:
    pass

count_p = int(input("Какое количество паролей Вам необходимо? Введите цифру:  "))

import random


chars_l_case = "qwertyuiopasdfghjklzxcvbnm"
chars_u_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
chars_numbers = "1234567890"


if l_case_count > 0:
    for i in range(l_case_count):
        p_l_case = ""
        while i != 0:
            p_l_case += random.choice(chars_l_case)
            i -= 1
else:
    pass

if u_case_count > 0:
    for i in range(u_case_count):
        p_u_case = ""
        while i != 0:
            p_u_case += random.choice(chars_u_case)
            i -= 1
else:
    pass

if numbers_count > 0:
    for i in range(numbers_count):
        p_num_case = ""
        while i != 0:
            p_num_case += random.choice(chars_numbers)
            i -= 1
else:
    pass

passwd_sum =""
if p_l_case != 0:
    passwd_sum = passwd_sum + p_l_case
elif p_u_case !=0:
    passwd_sum = passwd_sum + p_u_case
elif p_num_case !=0:
    passwd_sum = passwd_sum + p_num_case


for i in range(count_p):
    passw = ""
    for r in range(lenght_p):
        passw = passw + random.choice(passwd_sum)
    print(passw, end="\n")


