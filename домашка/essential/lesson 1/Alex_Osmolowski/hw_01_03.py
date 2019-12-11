# Задание 3
# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
# позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
# быть заданы в одной шкале, а получены в другой.


class Temperature(object):  # класс хранящий показания температуры
    def __init__(self, celsius=0):  # конструктор класса
        self.celsius = celsius

    @property  # проперти получения значения хранимой температуры в Фаренгейтах
    def fahrenheit(self):
        return self.celsius * 1.8 + 32

    @fahrenheit.setter  # проперти занесения хранимого значения температуры в Фаренгейтах
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

    def __str__(self):  #
        return 'Шкала Цельсия: {} С\nШкала Фаренгейта: {} F\n'.format(
            self.celsius, self.fahrenheit)


def main():
    temperature = Temperature(32)
    print(temperature)

    temperature.celsius = 0
    print(temperature)

    temperature.fahrenheit = 100
    print(temperature)

    temperature.fahrenheit = 122
    print(temperature)


if __name__ == '__main__':
    main()