# Задание 1 Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).
class Iter:
    def __init__(self, step = 1):
        self.step = step

    def __next__(self):
        self.step -= 1
        if self.step < 0:
             raise StopIteration()
        return self.step

    def __iter__(self):
        return self

a = Iter()
a.step = 20

for i in a:
    print(i)
