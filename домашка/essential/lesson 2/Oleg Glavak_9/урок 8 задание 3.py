class Cars:
    def __init__(self, brend, number):
        self.brend = brend
        self.number = number

    def __del__(self):
        print('Учет выполнен')

    def __str__(self):
        return f'В салоне продают авто брендa: {self.brend}'

    def __add__(self, other):
        return f"В салоне {self.number + other.number} авто Mersedes и Audi "

    def __sub__(self, other):
         return f"Автомобилей Audi больше чем BMW на {self.number - other.number}"

    def __truediv__(self, other):
        return f"Автомобилей Mersedes больше от BMW в {self.number / other.number} раза"

    def __mod__(self, other):

        return f"{self.number % other.number} деление по модулю."

    def __mul__(self, other):
        return f"{self.number * other.number} умножение"

    def __eq__(self, other):
        return {self.number == other.number}

    def __ne__(self, other):
        return {self.number != other.number}

    def __lt__(self, other):
        return {self.number < other.number}

    def __gt__(self, other):
        return{self.number > other.number}

    def __le__(self, other):
        return{self.number <= other.number}

    def __ge__(self, other):
        return {self.number >= other.number}

    def __bool__(self):
        return f""

    def __len__(self):
        print('Количество авто:')
        return int(self.number)

    def __int__(self):
        print(self.brend)
        return int(self.number)

Mazda = Cars('Mazda', 18)
Audi = Cars('Audi', 10)
BMW = Cars('BMW', 4)
Mersedes = Cars('Mersedes', 8)

print()
print(Mazda)
print(Audi)
print(BMW)
print(Mersedes)
print()
print(Audi + Mersedes)
print(Audi - BMW)
print(Mersedes / BMW)
print(Mazda % Audi)
print(BMW * Audi)
print()
print(Mazda == Audi)
print(Mersedes != BMW)
print(Mazda < Audi)
print(Mazda < Mersedes)
print(Audi <= BMW)
print(Mazda >= BMW)
print()
if not (Mersedes > Audi):
    print('автомобилей Audi больше')
    print(len(Audi))
    print(int(Audi))
else:
    print('автомобилей Mersedes больше')
    print(len(Mersedes))
    print(int(Mersedes))
print()