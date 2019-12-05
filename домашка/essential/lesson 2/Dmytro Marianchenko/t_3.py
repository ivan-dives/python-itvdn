class Guns:
    def __init__(self, gun, model, klass, calib):
        self.gun = gun
        self.model = model
        self.klass = klass
        self.calib = calib


class Fact(Guns):
    def __str__(self):
        return f"Производитель: {self.gun}"


class Model(Fact):
    def __str__(self):
        return f"Модель: {self.model}"


class Klass(Model):
    def __str__(self):
        return f"Класс: {self.klass}"


class Calib(Klass):
    def __str__(self):
        return f"Калибр: {self.calib}"


def main():
    # Guns("Remington", "Remington 700", "Нарезное", "7,62(х51,х67,х72), 5,56(х45), 6,2(х52), 8,6(х70)")
    print(object)
    print(Guns.__mro__)
    print(Fact.__mro__)
    print(Model.__mro__)
    print(Klass.__mro__)
    print(Calib.__mro__)


if __name__ == '__main__':
    main()
