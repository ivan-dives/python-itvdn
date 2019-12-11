# Задание 1
# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
# reversed).

class MyRevers(object):
    """Итератор, возвращающий последовательность в обратном порядке"""

    def __init__(self, seq):
        self.seq = seq
        self.ind = len(seq) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < 0:
            raise StopIteration

        value = self.seq[self.ind]
        self.ind -= 1

        return value


def main():
    # Перевернём строку
    my_str = "УЛЫБОК ТЕБЕ ДЕД МАКАР"
    for i in MyRevers(my_str):
        print(i, end="")
    print()

    # Перевернём последовательность степеней двойки
    my_seq = [1, 2, 4, 8, 16, 35, 64, 128, 256, 512, 1024]
    for i in MyRevers(my_seq):
        print(i, end='  ')


if __name__ == '__main__':
    main()