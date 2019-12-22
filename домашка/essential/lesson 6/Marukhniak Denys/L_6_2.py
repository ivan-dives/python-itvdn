# Задание 2
# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.

URLS = {}


def found_by_short(short):
    global URLS
    tmp = URLS.get(int(short[14:]), 'Short url is not created')
    return tmp


def add_n_get(url):
    global URLS
    short = abs(hash(url))
    URLS.setdefault(short, url)
    return 'short_url.biz/' + str(short)


while True:
    print('''
    Menu:
    1. Get short url from url
    2. Get original url from short url
    3. Stop
    ''')
    command_menu = int(input('Enter number: '))
    if command_menu == 1:
        url = input('Enter url: ')
        add_n_get(url)
        print(f'Your short url: {add_n_get(url)}')
    elif command_menu == 2:
        short_name_in = input('Enter short url: ')
        try:
            print(f'Your original url: {found_by_short(short_name_in)}')
        except ValueError:
            print('Incorrect short url.')
    if command_menu == 3:
        break
