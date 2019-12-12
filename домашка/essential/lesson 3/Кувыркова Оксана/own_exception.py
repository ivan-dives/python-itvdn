class MyError(Exception):
    def __init__(self):
        print("This ingridient ia not allowed in my recepy")

class Recepy():

    def ingridiens(self):
        recepy = []
        ingridient = str
        for i in range (5):
            try:
                ingridient = input("Name ingridient\n")
                if ingridient == "melon":
                    raise MyError
                recepy.append(ingridient)
            except MyError:
                MyError()

        print(f"Your ingridients are{recepy}")

apple_pie = Recepy()
apple_pie.ingridiens()


