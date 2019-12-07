class Check_pet:
    def __init__(self, func):
        self.func = func
    def __call__(self,*args,**kwargs):
        if kwargs != "Polkan":
            return "Here is your food, bro"
        else:
            return "You are not my dog"
@Check_pet
def pet_name(self, name):
    self.name = name
    return self.name

print(pet_name("Polkan"))
