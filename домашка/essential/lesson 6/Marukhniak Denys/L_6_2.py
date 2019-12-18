# Задание 2
# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.

URLS = {}


def add_new_url(url_add):
    global URLS
    short_name = abs(hash(url_add))
    tmp = {short_name: url_add}
    URLS.update(tmp)


def found_by_short(short):
    global URLS
    tmp = URLS.get(int(short[14:]), 'Short url is not created')
    return tmp


def get_short(url):
    global URLS
    short = abs(hash(url))
    tmp = URLS.get(short, 'Short url is not created')
    short_url = 'short_url.biz/' + str(short)
    return short_url


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
        add_new_url(url)
        print(f'Your short url: {get_short(url)}')
    elif command_menu == 2:
        short_name_in = input('Enter short url: ')
        try:
            print(f'Your original url: {found_by_short(short_name_in)}')
        except ValueError:
            print('Incorrect short url.')
    if command_menu == 3:
        break
