# Задание 1
# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

def main():
    str1 = set(input('INPUT L1 PLZ: '))
    str2 = set(input('INPUT L2 PLZ: '))
    print(str1)
    print(str2)
    print()
    print(str1 & str2)

if __name__ == '__main__':
    main()
