class Playing_frames:
    quantity = 4 # количество

    def __init__(self, suit, rank, priority):
        # self.name = name
        self.suit = suit # ранг
        self.rank = rank # масть
        self.priority = priority # Приоритетность

        print(f'Привет, теперь у тебя есть {self.suit} {self.rank}!')
        Playing_frames.quantity += 1

    def __del__(self):
        print(f'Ты походил картой {self.suit}! Этой карты у тебя больше нет.')
        Playing_frames.quantity -= 1
        if Playing_frames.quantity == 0:
            print(f'{self.suit} {self.rank} была последней картой если в подборе больше нет карт, поздравляем. ты победил.')
        else:
            print(f'У тебя осталось еще {Playing_frames.quantity} карты')

    def __add__(self, other):
        if Playing_frames.quantity >= 6:
            return f'эта карта лишняя ты не можешь ее подобрать'
        else:
            Playing_frames.quantity += 1
            return f'теперь у тебя {Playing_frames.quantity} карт'

    def __sub__(self, other):
        if self.priority < other.priority:
            return 'не жульничай'
        else:
            Playing_frames.quantity -= 1
            return f'{self.suit}  побил {other.suit}'

    def __mul__(self, other):
        if self.priority > other.priority:
            return f'теперь у вас есть козырный  {self.suit}'
        else:
            return f'теперь у вас есть козырный {other.suit}'

    def __truediv__ (self, other):
        if self.priority > other.priority:
            return f'теперь у вас есть козырный {other.suit}'
        else:
            return f'теперь у вас есть козырный {self.suit}'

    def __gt__(self, other):
        if self.priority > other.priority:
            return f'{self.suit} больше чем {other.suit}'
        else:
            return f'{other.suit} больше чем {self.suit}'

    def __str__(self):
        return f'У вас {self.suit}, масть -  {self.rank}, приоритетность - {self.priority} '


    def howMany():
        if Playing_frames == 1:
            print(f"У тебя на руках {Playing_frames.quantity} карта ")
        else:
            print(f"У тебя на руках {Playing_frames.quantity} карты ")


c = Playing_frames('Туз' ,'крести', 14) #Привет, теперь у тебя есть Туз крести!
b = Playing_frames('Валет', 'черви',11) # Привет, теперь у тебя есть Валет черви!
Playing_frames.howMany()  # У тебя на руках 6 карты
print(c - b) # Туз  побил Велет
print(b - c) # не жульничай
print(c+b) # теперь у тебя 6 карт
print(c+b) # эта карта лишняя ты не можешь ее подобрать
print(b*c) # теперь у вас есть козырный Туз
print(b/c) # теперь у вас есть козырный Валет
print(b>c) # Туз больше чем Валет
print(b<c) # Туз больше чем Валет
print(c) # У вас Туз, масть -  крести, приоритетность - 14
print(b) # У вас Валет, масть -  черви, приоритетность - 11
del b # Ты походил картой Велет! Этой карты у тебя больше нет. У тебя осталось еще 5 карты
del c # Ты походил картой Туз! Этой карты у тебя больше нет. У тебя осталось еще 4 карты
