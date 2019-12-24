"""
Модуль операци со ссылками (добавление и получение ссылок по короткому имени)
"""
def add_link_to(links):
    """Функция добавления новой ссылки в словарь links"""

    original_url = input('Введите ссылку: ')
    short_name = None
    while not short_name or short_name in links:
        short_name = input('Введите короткое имя: ')
        if short_name in links:
            print('Такое имя уже существует '
                  '(ссылка: {})'.format(links[short_name]))

    links[short_name] = original_url


def get_link_from(links):
    """Функция получения ссылки из словаря links"""

    name = input('Введите имя ссылки: ')
    url = links.get(name, None)

    if url:
        print(url)
    else:
        print('Такой ссылки не существует!')


def main():
    print(__doc__)


if __name__ == '__main__':
    main()

