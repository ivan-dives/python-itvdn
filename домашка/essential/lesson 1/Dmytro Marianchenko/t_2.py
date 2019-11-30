class Guns:
    model = 0
    country = 0
    calib = 0
    year = 0
    name = 0
    text = 0

    def __init__(self, model,calib,year,country,name,text):
        self.model = model
        self.country = country
        self.calib = calib
        self.year = year
        self.name = name
        self.text = text

    def __str__(self):
        return f"    Модель = {self.model}\n    Страна разработки = {self.country}\n    Калибр = {self.calib}\n    Год разработки = {self.year}\n\nПокупатель: {self.name}\n Отзыв: {self.text}\n"



gun1 = Guns("АК-47","7.62 (x39)","1947","СССР","Вова Ульянов","Очень надежный!! Пользуюсь с 48-го года")
gun2 = Guns("АК-74","5.45 (x39)","1974","СССР""","Рамзан К.","Подарыл малому на Нови Годе! Малой дАволены")
gun3 = Guns("UZI","9 (х19)","1954","Израиль","Хмед","هذه الأشياء فائقة")
gun4 = Guns("Remington 700","7,62(х51,х67,х72), 5,56(х45), 6,2(х52), 8,6(х70)","1962","США","Зайцев","Берите только в 308м калибре!! ")
print(gun1)
print(gun2)
print(gun3)
print(gun4)