"""Модуль консольного интерфейса приложения (главный можуль)"""

from links_storage import LinksSt


def add_link_to(links):
    """Функция добавления новой ссылки в хранилище links"""

    while True:
        short_name = input('Введите имя ссылки: ')
        original_url = input('Ввелите url: ')

        try:
            links.set_url(short_name, original_url)
        except (KeyError, ValueError) as error:
            print(error.args[0])
        else:
            break


def get_link_from(links):
    """Функция получения ссылки из хранилища links"""

    name = input('Введите имя ссылки: ')

    try:
        url = links.get_url(name)
    except KeyError:
        print('Ссылка с таким именем не найдена:', name)
    else:
        print(url)


def main():
    """Главная функция приложения"""

    links = LinksSt()
    f = {"1": add_link_to, "2": get_link_from, "3": exit}

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input('> ').strip()
        try:
            f[choice](links)
        except KeyError:
            print('Некорректный ввод пункта меню')
        print()


if __name__ == '__main__':
    main()