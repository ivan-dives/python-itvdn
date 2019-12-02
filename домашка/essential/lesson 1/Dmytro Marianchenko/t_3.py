class Temperature:

    def __init__(self, tempo, tempo_atr):
        self.tempo_atr = tempo_atr
        self.tempo = tempo
        self.sumo1 = (self.tempo - 32) / 1.8
        self.sumo2 = (self.tempo + 32) * 1.8

    def calc_temp(self):
        if self.tempo_atr == "f":
            return round(self.sumo1)
        elif self.tempo_atr == "c":
            return round(self.sumo2)

    def __str__(self):
        return f"{self.calc_temp()}"


atr = input("Что хотите сконвертировать Цельсьй или Фарингейт? (c / f):  \n")
number = int(input("Введите значение температуры:  \n"))
t1 = Temperature(number, atr)
print(t1)

