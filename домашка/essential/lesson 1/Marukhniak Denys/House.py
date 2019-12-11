# - ваш объект должен уметь печататься через print (подсказка __str__)
# - ваш объект должен уметь арифметику: + - / % *
# - ваш объект должен уметь сравнения < <= == >= >
# - ваш объект должен уметь not
# - ваш объект должен уметь if myobj (подсказка __bool__)
# - ваш объект должен уметь отвечать функции len (подсказка __len__)
# - ваш объект должен уметь сказать Привет в момент создания и Досвидания в момент смерти (подсказка __init__ __del__)
# - ваш объект должен уметь кастоваться в int()


class House:
    bricks = 400
    windows = 4
    doors = 1
    long = 10

    def __init__(self, n_bricks, n_windows, n_doors):
        self.bricks = n_bricks
        self.windows = n_windows
        self.doors = n_doors
        print(f'Начинаем постройку дома')

    def __del__(self):
        print('Построили')

    def __str__(self):
        return f"Дом состоит из:\n" \
               f"{self.bricks} - кирпичей\n" \
               f"{self.windows} - окон\n" \
               f"{self.doors} - дверей"

    # >>> (+ - / % *)
    def __add__(self, other):
        return f"В домах сумарно {self.bricks + other.bricks} кирпичей"

    def __sub__(self, other):
        return f"Во втором доме кирпичей меньше на {self.bricks - other.bricks}"

    def __truediv__(self, other):
        return f"В первом доме окон больше на {self.windows - other.windows}"  # /

    def __mod__(self, other):
        return f"В домах {self.doors + other.doors} дверей"  # %

    def __mul__(self, other):
        return f"В домах {self.windows + other.windows} окон"  # *

    # >>> (< <= == >= >)
    def __lt__(self, other):
        return f"Площадь первого дома меньше: " \
               f"{self.bricks + self.windows*30 + self.doors*50 < other.bricks + other.windows*30 + other.doors*50}"

    def __le__(self, other):
        return f"Площадь первого дома меньше или равна: " \
               f"{self.bricks + self.windows*30 + self.doors*50 <= other.bricks + other.windows*30 + other.doors*50}"

    def __eq__(self, other):
        return f"Площадь первого дома равна площаде второго: " \
               f"{self.bricks + self.windows*30 + self.doors*50 == other.bricks + other.windows*30 + other.doors*50}"

    def __ge__(self, other):
        return f"Площадь первого дома больше или равна: " \
               f"{self.bricks + self.windows*30 + self.doors*50 >= other.bricks + other.windows*30 + other.doors*50}"

    def __gt__(self, other):
        return f"Площадь первого дома больше: " \
               f"{self.bricks + self.windows*30 + self.doors*50 > other.bricks + other.windows*30 + other.doors*50}"

    # >>> (bool, len, int)
    def __bool__(self):
        return f"Дом строится"

    def __len__(self):
        print('Высота дома:')
        return int((self.bricks + self.windows*30 + self.doors*50) / (self.long * 4))

    def __int__(self):
        print('Окон и дверей:')
        return self.windows+self.doors


first = House(600, 5, 1)
print()
second = House(550, 4, 1)
print('----------------------')
print(first)
print()
print(second)
# >>> (+ - / % *)
print('----------------------')
print(first + second)
print(first - second)
print(first / second)
print(first % second)
print(first * second)
# >>> (< <= == >= >)
print('----------------------')
print(first < second)
print(first <= second)
print(first == second)
print(first >= second)
print(first > second)
# >>> (bool, len, int)
print('----------------------')
if not (first > second):
    print('Второй дом больше первого')
    print(len(second))
    print(int(second))
else:
    print('Первый дом больше второго')
    print(len(first))
    print(int(first))
print('----------------------')
