# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
# транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
# Выведите информацию о каждом транспортном средстве.


class Vehicles:
    max_speed = 100  # k/h
    capacity = 6

    def __str__(self):
        return f'{self.max_speed=}, {self.capacity=}'


class Carriage(Vehicles):
    horses = 2

    def __str__(self):
        return f'{self.horses=}, {self.capacity=}'


class RecyclingTruck(Vehicles):
    employees = 2

    def __str__(self):
        return f'{self.employees=}'


class DumpTruck(Vehicles):
    load_capacity = 2000

    def __str__(self):
        return f'{self.load_capacity=}, {self.max_speed=}'


Vehicle1 = Carriage()
Vehicle2 = RecyclingTruck()
Vehicle3 = DumpTruck()

print(Vehicle1)
print(Vehicle2)
print(Vehicle3)
