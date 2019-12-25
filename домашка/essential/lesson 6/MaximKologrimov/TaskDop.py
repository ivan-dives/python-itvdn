# Задание
# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
# произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
# указывая параметры.

idbook = {'Vasia': '234-424', 'Kolia': '547-643', 'Yulia': '234-395', 'Ksusha': '678-164'}

def foo(**kwargs):
    print('item', idbook.items())
    print('keys', idbook.keys())
    print('values', idbook.values())
    print()
    for key in kwargs.keys():
        print('NAME =', key)
    print()
    for value in kwargs.values():
        print('ID =', value)

    for x, y in kwargs.items():
        print(f'Сотрудник {x}, с присвоенным ID {y}')


foo(**idbook)