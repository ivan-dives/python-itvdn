
class Car:
    __color = 'white'
    __passengers = 4

    def __init__(self, new_color, passengers):
        self.__color = new_color
        self.__passengers = passengers

    def __str__(self):
        return f"I am a car, my color is {self.__color}, {self.__passengers} passengers"

c = Car('blue', 2)
#print(c.tell_me_your_color())
print(c)
#c == 'volvo'
#print(c)
#print(10)
#print(1.0)

exit()

class Wallet:
    __money = 100

    def __check_owner(self):
        name = input('what is your name? ')
        return name == 'ivan'

    def how_much_money(self):
        if not self.__check_owner():
            print("I do not know you")
        else:
            print(f"I have {self.__money} hryvnas")


w = Wallet()
#w.money = 100
#w.money -= 50
#w.__money = 50
#w.__check_owner()
w.how_much_money()
exit()

class Car:
    #passengers = []
    speed = 0

    def change_speed(self, new_speed):
        print(f'called change_speed for car {id(self)}, new_speed={new_speed}')
        self.speed = new_speed


mycar = Car()
#print(f'created mycar, id={id(mycar)}')
#print(mycar.speed)
mycar.change_speed(10)
print(f"mycar: {id(mycar)}, mycar.speed {id(mycar.speed)}")
#Car.change_speed(mycar, 10)
#print(mycar.speed)

yourcar = Car()
#print(f'created yourcar, id={id(yourcar)}')
#print(yourcar.speed)
yourcar.change_speed(20)
print(f"yourcar: {id(yourcar)}, yourcar.speed {id(yourcar.speed)}")
#print(yourcar.speed)
