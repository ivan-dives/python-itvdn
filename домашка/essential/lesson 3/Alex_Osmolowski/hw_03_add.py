# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.


class CodeWordError(Exception):
    def __init__(self, code_word=None, msg=None):
        if not code_word:
            self.__code_word = "exit"
        else:
            self.__code_word = code_word.strip().strip().lower()
        if not msg:
            self.__msg = "Введено кодовое слово"
        else:
            self.__msg = msg

    def __str__(self):
        return f'{self.__msg}: {self.__code_word}'

    def check_word(self, wrd):
        return self.__code_word == wrd.strip().lower()


def inp_code_wrd(ex_obj):
    wrd = input("Введите кодовое слово: ")
    if ex_obj.check_word(wrd):
        raise ex_obj


def main():
    my_exc = CodeWordError()
    while True:
        try:
            inp_code_wrd(my_exc)
        except CodeWordError:
            print(my_exc)
            return
        finally:
            print()


if __name__ == '__main__':
    main()
