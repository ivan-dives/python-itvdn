
z = input('Введи Ваше имя: ')
def foo(name):

    if not name:
        print('Вас зовут Вадим? (y/n)')
        x = input('>>>>')
        if x.lower() == 'y':
            x = print("Приветствую тебя Вадим, меня тоже создал Вадим")
        else:
            x = print("Печальненько что ты не Вадим :(")
        return x
    print(f'Приветствую тебя {name}!')

foo(z)