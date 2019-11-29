class Water:
    def __init__(self, fish, quantity, size, eat):
        self.fish = fish
        self.quantity = quantity
        self.size = size
        self.eat = eat
        print(f"Привет, обьект {fish} создан")

    def __del__(self):
        print(f"Обьект {self.fish} удален(")

    def __str__(self):
        return f"{self.fish} количеством {self.quantity}"

    def __add__(self, other):
        return f"В водоеме {self.quantity + other.quantity} жителей"

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return f"В водоеме {self.quantity - other.quantity} жителей"
        else:
            s = (other.quantity + self.quantity) - self.quantity
            return f"В водоеме {s} жителей"

    def __mul__(self, other):
        name = self.fish[0:2] + other.fish[2::]
        s = self.quantity * other.quantity
        return f"Позравляю тепер у нас {s} {name}"

    def __truediv__(self, other):
        if self.fish == "Хищник":
            return f" Травоядное не может съесть хищника"
        else:
            s = other.quantity / self.quantity
            return f"Каждый хощник съел {s} травоядных"

    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.size > other.size:
            return True
        else:
            return False




crucian = Water("Карась", 100, 10, "Хищник")
shurk = Water("Акула", 2, 50, "Травоядный")
print(crucian)
print(shurk)
t = crucian + shurk
z = shurk - crucian
r = shurk * crucian
print(t)
print(z)
print(r)
print(shurk > crucian)
print(shurk < crucian)

