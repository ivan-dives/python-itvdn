class Test:
    def __init__(self, fish, size):
        self.fish = fish
        self.size = size
        print(f"Привет, обьект {fish} создан")

    def __del__(self):
        print(f"Обьект {self.fish} удален(")

    def __str__(self):
        return f"{self.fish} размером {self.size}"

    def __add__(self, other):
        return self.fish[0:2] + other.fish[1::]

    def __sub__(self, other):
        return self.fish[1::] + other.fish[2::]






crucian = Test("Карась", 3)
shurk = Test("Акула", 10)
print(crucian)
print(shurk)
t = crucian + shurk
z = shurk - crucian
print(t)
print(z)

