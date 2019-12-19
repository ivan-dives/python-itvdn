# Задание 1
# Даны две строки. Выведите на экран символы, которые есть в обоих строках.


def main():
    first_string = input('Введите превую строку: ')
    second_string = input('Введите вторую строку: ')
    print(''.join(set(first_string) & set(second_string)))


if __name__ == '__main__':
    main()