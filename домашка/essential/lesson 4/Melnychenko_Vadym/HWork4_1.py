class Revers:
    def __init__(self, object):
        self.object = object
        self.index = len(object) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.object[self.index]
        self.index -= 1

        return value


def relise():
    reli = list(input('Введите слово/предложение: '))
    for i in Revers(reli):
        print(i)


relise()
