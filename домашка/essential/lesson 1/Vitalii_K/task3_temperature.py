class Temperature:
    def __init__(self):
        self.__t = -273.15 #Celsius
    @property
    def c(self):
        return self.__t
    @c.setter
    def c(self, t):
        self.__t = round(t, 2)
    @property
    def f(self):
        return round(self.__t * 1.8 + 32, 2)
    @f.setter
    def f(self, t):
        self.__t = round((round(t, 2) - 32) / 1.8, 2)
        round(self.__t, 2)

human = Temperature()
human.c = 36.66
print(f'{human.f}°F - normal body temperature')
human.f += 4.44
print(f'{human.c}°C - fever')
