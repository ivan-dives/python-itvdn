def check_name(method):
    def condition(name_atr):
        if name_atr.name == "Polkan":
            print ("Here is your food, bro")
        else:
            method(name_atr)
    return condition


class Introducing:
    def __init__(self, name):
        self.name = name
    @check_name
    def print_introducion(self):
        print ("The pet name is", self.name)

p = Introducing("Polkan")
p.print_introducion()

p = Introducing("Amur")
p.print_introducion()