# Задание 1
# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
# интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
# замене последнего на другой, взаимодействующий с пользователем иным способом, программа
# должна продолжать корректно работать.
import short_url as su


def main():
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
            su.add_n_get(url)
            print(f'Your short url: {su.add_n_get(url)}')
        elif command_menu == 2:
            short_name_in = input('Enter short url: ')
            try:
                print(f'Your original url: {su.found_by_short(short_name_in)}')
            except ValueError:
                print('Incorrect short url.')
        if command_menu == 3:
            break


if __name__ == '__main__':
    main()
