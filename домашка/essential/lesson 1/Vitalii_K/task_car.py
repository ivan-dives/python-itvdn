class Car:
    def __init__(self, man=None, mod=None, year=None, price=0):
        self.man = man
        self.mod = mod
        self.year = year
        self.price = price

    def __str__(self):
        return '{} {} {}'.format(self.man, self.mod, self.year)


class Dealer:
    cars = []

    def __init__(self, name=None, money=0):
        self.name = name
        self.money = money

    def __str__(self):
        return f'{self.name}'

    def moto(self, moto):
        self.moto = moto

    def buy_car(self, car):
        if car.price > 0:
            if self.money >= car.price / 2:
                car.price /= 2  # Monty knows how to haggle...
                car.price = round(car.price)
                self.money -= car.price
                print(f'{car} has been bought for {car.price}!')
                print(self.moto)
                car.price *= 4  # Monty knows how to sell for profit!
                self.cars.append(car)
            else:
                print(f'"{self.name}" have no interest in buying your car.')
        else:
            print('Find another car dealership to scam!')

    def sell_car(self, car):
        self.money += car.price
        print(f'{car} has been sold for {car.price}!')
        print(self.moto)
        car.price /= 2 #Best deals at "Monty's Muscles"!
        self.cars.remove(car)

    def car_list(self):
        for car in self.cars:
            print(f'{self.cars.index(car) + 1}. {car} - {car.price} USD')


c1 = Car('Ford', 'Mustang Shelby GT500', '1968', 125000)
c2 = Car('Dodge', 'Charger Daytona','1969', 235000)
c3 = Car('Pontiac', 'GTO "The Judge"', '1969', 85000)
c4 = Car('Plymouth', 'Barracuda', '1970', 110000)

d = Dealer("Monty's Muscles", 500000)
d.moto(f'***Best deals at "{d.name}"***')
d.cars.append(c1)
d.cars.append(c2)
d.cars.append(c3)
d.cars.append(c4)

print("Hello there! I bet you've always dreamed...\n"\
      'about your own brand new (or not so) shiny muscle car...\n'\
      "And you know what? You've come to the right place!\n"\
      f'Here at "{d}" we have all your heart will ever desire...\n'\
      'Damn! That must be the luckiest day of your life!\n'\
      '*You can also sell your car for a good price (probably)*\n'
      f'{d.moto}\n')

while True:
    a = input('Enter "1" if you want to buy a car...\n' \
              'Enter "2" if you want to sell a car...\n' \
              'Enter "0" if you want to buy (or sell) a car ' \
              'but have no money( or car)...\n')
    if a == '1':
        d.car_list()
        print('Enter the number of the car you want to buy: ')
        aa = int(input())
        d.sell_car(d.cars[aa-1])
        break
    if a == '2':
        print('Define your car, please...')
        q = input('Manufacturer: ')
        w = input('Model: ')
        e = input('Year: ')
        r = int(input('Price:'))
        t = Car(q, w, e, r)
        d.buy_car(t)
        break
    if a == '0':
        break
    else:
        continue
