import random

sum = ""
alpha = "qwertyuiopasdfghjklzxcvbnm"
beta = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
special = "@#$%{}[]()/'\"\\,;:.<>"

print("""Choose simbol you wont to use in your password:
1. Add lower letters
2. Add upper letters
3. Add numbers
4. Add special simbols
5. Continue""")


while True:
    choose = int(input(">"))
    if choose == 1:
        sum = sum + alpha
        print("You add lower letters")
    elif choose == 2:
        sum = sum + beta
        print("You add upper letters")
    elif choose == 3:
        sum = sum + number
        print("You add numbers")
    elif choose == 4:
        sum = sum + special
        print("You add special simbols")
    elif choose == 5:
        print("Continue")
        break
    else:
        pass

k = int(input("Howe many passwords do you need: "))
r = int(input("Passwords length"))




for i in range (k):
    password = ""
    for j in range(r):
        password += random.choice(sum)
    print(password, end="\n")

