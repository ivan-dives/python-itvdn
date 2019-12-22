# Задание
# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте
# отдельные его имена.
import os
import pprint
import sys


def main():
    lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'lesson 4', 'Marukniak Denys'))
    sys.path.insert(0, lib_path)
    import L_4_add
    # pprint.pprint(sys.path)
    # print(os.path.join(__file__))


if __name__ == '__main__':
    main()
