class PowError(Exception):
    pass

def errors(f):
    def tmp(n):
        try:
            r = f(n)
            print(f"Result = {r}")
        except ArithmeticError as error:
            print("Error", error)
    return  tmp


class Calc:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @errors
    def add(self):
        return self.x + self.y

    @errors
    def sub(self):
        return  self.x - self.y

    @errors
    def mul(self):
        return  self.x * self.y

    @errors
    def div(self):
        return  self.x / self.y

    @errors
    def pow(self):
        if self.x == 0 and self.y < 0:
            raise PowError("You can not pow 0 in neg value")
        else:
            return self.x ** self.y



while True:
    x = int(input("Enter first operand: "))
    y = int(input("Enter second operand: "))

    calc = Calc(x, y)

    print("""Choose an operation:
    1. Adding
    2. Subtraction
    3. Multiplication
    4. Division
    5. Pow
    6. Exit""")

    choose = int(input(">"))

    if choose == 1:
        calc.add()
    elif choose == 2:
        calc.sub()
    elif choose == 3:
        calc.mul()
    elif choose == 4:
        calc.div()
    elif choose == 5:
        try:
            calc.pow()
        except PowError as error:
            print("Error", error)
    else:
        print("Exit")
        break