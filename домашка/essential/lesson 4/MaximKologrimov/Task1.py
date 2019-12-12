# Задание 1
# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
# reversed).

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


list = Reverse([1, 2, 3, 4, 5])
iter(list)

for n in list:
    print(n)
