# Задание 1
# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если
# имя не указано, она должна выводить приветствие для пользователя с Вашим именем.

name = input('Введите имя: ')
print()

def user1():
    if name:
        print(f'Hello {name}!!!')
    else:
        print(f'Hello Max!!!')

def user2(x):
    if x:
        print(f'Hello {x}!!!')
    else:
        print(f'Hello Max!!!')

user1()
print()
user2(name)
