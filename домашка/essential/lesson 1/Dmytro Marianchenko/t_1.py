class Guns:
    model = 0
    country = 0
    calib = 0
    year = 0

    def __init__(self, model,calib,year,country):
        self.model = model
        self.country = country
        self.calib = calib
        self.year = year
    def __str__(self):
        return f"    Модель = {self.model}\n    Страна разработки = {self.country}\n    Калибр = {self.calib}\n    Год разработки = {self.year}\n"

gun1 = Guns("АК-47","7.62 (x39)","1947","СССР")
gun2 = Guns("АК-74","5.45 (x39)","1974","СССР")
gun3 = Guns("UZI","9 (х19)","1954","Израиль")
gun4 = Guns("Remington 700","7,62(х51,х67,х72), 5,56(х45), 6,2(х52), 8,6(х70)","1962","США")
print(gun1)
print(gun2)
print(gun3)
print(gun4)