import random

while True:
    length = int(input("Please input length of password min 6: "))
    count = int(input("Please input number of passwords min 1: "))
    if length >= 6 and count >= 1:
        break
    print("repeat")

while True:
    choice_bool = True
    choice = input("Do you need special symbols Y/N (yes or no): ")
    if choice.lower() == "y" or choice.lower() == "yes":
        choice_bool = True
        break
    elif choice.lower() == "n" or choice.lower() == "no":
        choice_bool = False
        break
    else:
        print("Enter  Y/N (yes or no)")


def password(length=6, choice=False):
    password = ""
    x = 3
    if choice:
        x = 4
    for i in range(length):
        use_symbol = random.randint(1, x)
        if use_symbol == 1:
            password += chr(random.randint(48, 57)) # Numbers
        elif use_symbol == 2:
            password += chr(random.randint(65, 90)) # Upper case
        elif use_symbol == 3:
            password += chr(random.randint(97, 122)) # Low case
        elif use_symbol == 4:
            password += chr(random.randint(33, 47))
    return password


def pass_generator(count, length, choice):
    return [password(length, choice) for i in range(count)]


print(*pass_generator(count, length, choice_bool), sep="\n")



