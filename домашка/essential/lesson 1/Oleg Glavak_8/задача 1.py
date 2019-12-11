class Books:
    def __init__(self, name, author, publishing, cat):
        self.name = name
        self.author = author
        self.publishing = publishing
        self.cat = cat

    def __str__(self):
        print(self.name, self.author, self.publishing, self.cat)

    def __repr__(self):
        print(self.name, self.author, self.publishing, self.cat)

    def __eq__(self, other):
        return self.name == other.name, self.author == other.author, self.publishing == other.publishing, self.cat == other.cat

    def __ne__(self, other):
        return self.name == other.name, self.author == other.author, self.publishing == other.publishing, self.cat == other.cat



book1 = Books('Зеленая миля', 'Стивен Кинг', 2017, 'Мистика')
book2 = Books('Скорбь Сатаны', 'Мария Корелли', 2019, 'Мистика')
book3 = Books('Выхода нет', 'Тэйлор Адамс', 2019, 'Детектив')
book4 = Books('Психология бессознательного', 'Карл Густав Юнг', 2012, 'Психология')

book1.__str__()
book2.__str__()
book3.__str__()
book4.__str__()

book1.__repr__()
book2.__repr__()
book3.__repr__()
book4.__repr__()

class Reviews:
    def __init__(self, rev):
        self.rev = rev

    def __str__(self):
        return self.rev