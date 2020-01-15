class God():
    def __init__(self):
        self.holiness = 100
        self.commandments = 10

    def self_identification(self):
        print("I am God")

class Human(God):
    def __init__(self):
        self.holiness = 50
        self.hands = 2
        self.legs = 2
        self.had = 1

    def self_identification(self):
        if self.holiness == 100:
            God.self_identification(self)
        else:
            print("I am Human")

    def skills(self, holiness):
        if self.holiness == 100:
            print("I can hill")
        else:
            print("i can multiply")


class Adam(Human):
    def __init__(self):
        super(Adam, self).__init__()

    def self_identification(self):
        super(Adam, self).self_identification()
        print("I am Man")


class Eva(Human):
    def __init__(self):
        super(Eva, self).__init__()

    def self_identification(self):
        super(Eva, self).self_identification()
        print("I am Woman")


class Man(Adam):
    def __init__(self):
        super(Man, self).__init__()

    def action(self):
        print("I kill animals")


class Woman(Eva):
    def __init__(self):
        super(Woman, self).__init__()

    def holiness(self, holiness):
        self.holiness = 30

    def action(self):
        print("I cook food")


class Hesus(Man):
    def __init__(self):
        God.__init__(self)

    def action(self):
        pass

woman = Woman()
woman.self_identification()
woman.action()
woman.skills(30)

man = Man()
man.self_identification()
man.action()
man.skills(30)

man1 = Hesus()
man1.self_identification()
man1.action()
man1.skills(100)

def main():
    print(Woman.mro())
    print(Man.mro())
    print(Hesus.mro())

if __name__ == '__main__':
    main()
