# Задание 1
# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
# reversed).


class Revers:
    def __init__(self, string):
        self.string = string
        self.index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.index -= 1
            if self.index < 0:
                raise StopIteration
            liter = self.string[self.index]
            return liter


string_1 = input('Enter a string: ')
first = Revers(string_1)
print('Reversed string: ', end='')

for x in first:
    print(x, end='')
