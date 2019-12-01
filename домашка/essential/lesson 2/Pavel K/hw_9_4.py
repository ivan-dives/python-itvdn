class Venicle:

    def __init__(self, color='white', speed='0', engine='2000'):
        self.color = color
        self.speed = speed
        self.engine = engine

    def to_print(self):
        return f'{self.color},{self.speed},{self.engine}'

    def first_cross(self, direction):
        return f'Впереди себя вы видите перекреток {direction}'

    def ferry(self, direction): #
        return f'Вы проехали еще немного и вот впереди себя вы видите паром {direction}'

    def tunnel(self, direction):
        return f'Впереди вас тунель {direction}'


class Bus(Venicle):

    def __init__(self, color='white', speed='0', engine='2000', seating=20):
        print('Create Bus')
        self.seating = seating
        super().__init__(color, speed, engine)

    def first_cross(self):
        return super().first_cross(
            f'так как вы едите на автобусе и у вас {self.seating} пасажиров, это дает вам право ехать прямо')

    def ferry(self):
        return super().ferry(
            f' за каждого пасажира вам нужно заплатить 5 евро, соберите с пассажиров {self.seating * 5} евро и переправляйтесь через паром.')

    def tunnel(self):
        return super().tunnel(
            f'Вы не можете им поехаеть, у вас полный салон детей которые начнут вопить, ищите другой путь')

    def __str__(self):
        return "Bus - " + super().to_print() + f" with {self.seating} seats\n"


class MotoBike(Venicle):

    def __init__(self, color='white', speed='0', engine='2000', sidecar=True):
        print('Create Motobike')
        self.sidecar = bool(sidecar)  # преобразуем число в бул
        super().__init__(color, speed, engine)

    def first_cross(self):
        if self.sidecar == True:
            return super().first_cross('У вас мотоцикл с каляской поэтому едите в общей полосе.')
        else:
            return super().first_cross(
                'так как вы без каляски сьежайте на велосипедную полосу и развлекитесь как следует.')

    def ferry(self):
        if self.sidecar == True:
            return super().ferry(f'Ваш мотоцикл с коляской за которую вам прийдется доплатить 10 евро.')
        else:
            return super().ferry(f'Так как у вас нет коляски проезд для вас всего 2 евро.')

    def tunnel(self):
        return super().tunnel(f'едьте смелей это ваш звездый час.')

    def __str__(self):
        if self.sidecar == True:
            return "Motobike " + super().to_print() + f" you have sidecar\n"
        else:
            return "Motobike " + super().to_print() + "\n"


class Truck(Venicle):

    def __init__(self, color='white', speed='0', engine='2000', capacity='10 тон'):
        print('Create Truck')
        self.capacity = capacity
        super().__init__(color, speed, engine)

    def first_cross(self):
        return super().first_cross(
            f'Так как вы едите на грузовике весом {self.capacity} вам нужно свернуть налево на перекрестке и выехать на обьездную.')

    def ferry(self):
        return super().ferry(
            f' за каждую тону веса вам нужно доплатить 20 евро, итог {self.capacity * 20} евро вам нужно для переправы.')

    def tunnel(self):
        return super().tunnel(f'высота тунеля 4 метро, посмитре помещаетесь ли вы?')

    def __str__(self):
        return "Truck - " + super().to_print() + f"  {self.capacity}\n"


truck = Truck(color='black', speed=80, engine=5000, capacity=30)
moto = MotoBike(color='yellow', speed=120, engine=1200, sidecar=0)
bus = Bus(color='white', speed=60, engine=1200, seating=30)
moto1 = MotoBike(color='red', speed=90, engine=1300, sidecar=3)

list = [truck, moto, moto1, bus]
print('---------------------------')
for obj in range(3):
    print(list[obj])
    print(list[obj].first_cross())
    print(list[obj].ferry())
    print(list[obj].tunnel())
    print('---------------------------')