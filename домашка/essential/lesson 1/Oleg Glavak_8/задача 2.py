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
        return self.name == other.name and self.author == other.author and self.publishing == other.publishing and self.cat == other.cat

    def __ne__(self, other):
        return self.name != other.name or self.author != other.author or self.publishing != other.publishing or self.cat != other.cat

book1 = Books('Зеленая миля', 'Стивен Кинг', 2017, 'Мистика')
book2 = Books('Скорбь Сатаны', 'Мария Корелли', 2019, 'Мистика')
book3 = Books('Выхода нет', 'Тэйлор Адамс', 2019, 'Детектив')
book4 = Books('Психология бессознательного', 'Карл Густав Юнг', 2012, 'Психология')

book1.__repr__()
book2.__repr__()
book3.__repr__()
book4.__repr__()

class Reviews:
    def __init__(self, rev):
        self.rev = rev

    def __str__(self):
        return self.rev

rev1 = Reviews('''Роман-событие, ставший лауреатом премии Брэма Стокера и вдохновивший Фрэнка Дарабонта
     на создание культового фильма, в котором Том Хэнкс сыграл, возможно, свою лучшую роль.
     …Стивен Кинг приглашает читателей в жуткий мир тюремного блока смертников, откуда уходят, чтобы не вернуться,
      приоткрывает дверь последнего пристанища тех, кто преступил закон и теперь отсчитывает последние часы... 
      До предела обнажены нервы, накалены страсти и обострены чувства. Уже ничего нельзя исправить — последняя черта 
      совсем близко. Но еще можно понять и посочувствовать тем, кому предстоит отправиться по зловещей Зеленой миле 
      в никуда…''')
rev2 = Reviews('''Молодой писатель Джеффри Темпест, прозябающий в нищете и безвестности, продает душу Сатане 
    и получает от Князя Тьмы все, о чем только мечтал… точнее, почти все. Теперь светское общество, ранее им пренебрегавшее, 
    лежит у его ног. К его услугам несметное состояние, любовь прекрасной девушки, роскошь и удовольствия.
     Но много ли это значит, если утрачено главное, ради чего Джеффри жил, — его талант?..''')
rev3 = Reviews('''Снежная буря. Маленький мотель в горной глуши, отрезанный от всего мира. 
    Мотель, в котором укрывается от разбушевавшейся стихии горстка автомобилистов. Одна из них – студентка Дарби Торн – 
    тщетно пытается поймать на автостоянке сигнал сотовой связи и внезапно видит мелькнувшую в заднем стекле
     припаркованного фургона детскую руку. В машине заперт похищенный ребенок! Как его спасти? Что предпринять? 
     До полиции не дозвониться. Доверять нельзя никому из "товарищей по несчастью" – ведь преступником может оказаться любой из них. 
     А это значит, что Дарби предстоит в одиночку вступить в смертельную схватку…''')
rev4 = Reviews('''В данном томе публикуются две программные работы Юнга: "О психологии бессознательного" 
    и "Отношения между Я и бессознательным". В этих работах автор развивает основные положения аналитической психологии,
    подробно раскрывая перед читателем ключевые понятия своей теории и свой метод в целом.''')

book1.__str__()
print(rev1.__str__())
book2.__str__()
print(rev2.__str__())
book3.__str__()
print(rev3.__str__())
book4.__str__()
print(rev4.__str__())
