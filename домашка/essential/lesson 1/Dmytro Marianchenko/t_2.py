class Guns:

    def __init__(self, model, calib, year, country):
        self.model = model
        self.country = country
        self.calib = calib
        self.year = year

    def __str__(self):
        return f"    Модель = {self.model}\n    Страна разработки = {self.country}\n    Калибр = {self.calib}\n    " \
               f"Год разработки = {self.year}\n "


class Comment:

    def __init__(self, name="Аноним", text="Пока нет отзывов.."):
        self.name = name
        self.text = text

    def __str__(self, name="Аноним", text="Нет отзывов"):
        return f"Покупатель: {self.name}\n    Отзыв: {self.text}"


gun1 = Guns("АК-47", "7.62 (x39)", "1947", "СССР")
comm1 = Comment("Вова Ульянов", "Очень надежный!! Пользуюсь с 48-го года")
gun2 = Guns("АК-74", "5.45 (x39)", "1974", "СССР")
comm2 = Comment("Рамзан К.", "Подарыл малому на Нови Годе! Малой дАволены")
gun3 = Guns("UZI", "9 (х19)", "1954", "Израиль")
comm3 = Comment("Ахмед", "هذه الأشياء فائقة")
gun4 = Guns("Remington 700", "7,62(х51,х67,х72), 5,56(х45), 6,2(х52), 8,6(х70)", "1962", "США")
comm4 = Comment(text="Берите только в 308м калибре!!!")
print(gun1, comm1)
print(gun2, comm2)
print(gun3, comm3)
print(gun4, comm4)
