def main():
    stroka1 = input('Введите 1 текст с клавиатуры: ')
    stroka2 = input('Введите 2 текст с клавиатуры: ')
    print(''.join(set(stroka1) & set(stroka2)))


if __name__ == '__main__':
    main()
