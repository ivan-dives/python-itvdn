# Задание 2
# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.


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
        print(name, ' - такое имя ссылки отсутствует!')


def main():
    """Главная функция приложения"""

    links = {}

    while True:
        print('1. Добавить ссылку')
        print('2. Показать ссылку')
        print('3. Выход')

        f = {"1": add_link_to, "2": get_link_from}

        choice = input('> ').strip()
        try:
            f[choice](links)
        except Exception as ex:
            print(ex)
        if choice == '1':
            add_link_to(links)
        elif choice == '2':
            get_link_from(links)
        elif choice == '3':
            break
        else:
            print('Некорректный ввод пункта меню')

        print()


if __name__ == '__main__':
    main()