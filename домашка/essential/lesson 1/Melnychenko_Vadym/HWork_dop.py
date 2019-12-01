# - ваш объект должен уметь печататься через print (подсказка __str__)
# - ваш объект должен уметь арифметику: + - / % *
# - ваш объект должен уметь сравнения < <= == >= >
# - ваш объект должен уметь not
# - ваш объект должен уметь if myobj (подсказка __bool__)
# - ваш объект должен уметь отвечать функции len (подсказка __len__)
# - ваш объект должен уметь сказать Привет в момент создания и Досвидания в момент смерти (подсказка __init__ __del__)
# - ваш объект должен уметь кастоваться в int()
# - ваш объект должен поддерживать любой метод (подсказка __getattr__)

class Special:

    eat = '0'
    move = '0'
    sleep = '0'

    def __init__(self, eat, move, sleep):
        self.eat = eat
        self.move = move
        self.sleep = sleep
        print(f"Привет, я жираф Том", '\n')

    def __str__(self):
        return f'''Мне хватит {self.eat} листиков, я наелся! 
        Теперь я могу пройти {self.move} шагов, на потом мне нужно поспать {self.sleep} часов. \n'''

    def __sub__(self, hod):
        self.move = int(self.move)
        hod = 100 - self.move
        return f'Я прошел {self.move} шагов, а мне нужно пройти 100 шагов, осталось пройти еще {hod} \n'

    def __add__(self, hod):
        self.move = int(self.move)
        hod = 7 + self.move
        if hod < 100:
            return f'Еще могу пройти - {hod}, потом мне нужно покушать. \n'
        else:
            return "Мне нужно поспать! \n"


    def __del__(self):
        del self.sleep
        return f'hocju spat {self.sleep}'


girafe_tom = Special(input('Съешь: '), input('Пройди: '), input('Поспи: '))
print(girafe_tom)
print(girafe_tom.__sub__(9))
print(girafe_tom.__add__(99))
#-----------------------------------------------------------
print("Не успел дописать, позже допишу, залью.")
#-----------------------------------------------------------
print(girafe_tom.__del__())