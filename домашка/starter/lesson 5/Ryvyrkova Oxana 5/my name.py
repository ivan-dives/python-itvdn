
def greeting(name):
    # Если имя пустое, выходим из функции
    if not name:
        return print("Hello, Oxana, wellcome back")
    print(f'Hello, user {name}.')


greeting(input('Dear, user, what is your name \n'))