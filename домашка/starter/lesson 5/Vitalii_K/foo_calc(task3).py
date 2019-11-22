def calc_add(a, b):
    return a + b
def calc_sub(a, b):
    return a - b
def calc_mult(a, b):
    return a * b
def calc_div(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisor must not be zero! OBVIOUSLY!"
while True:
    print("Enter '1' if u want to calculate.",
          "Enter '0' if u want to exit.", sep='\n')
    j = input()
    if j == "1":
        op = input("Enter operation ('+', '-', '*', '/'): ")
        if op != "+" and op != "-" and op != "*" and op != "/":
            print("Read the parentheses part, plese...")
        else:
            x = input("Enter the number: ")
            try:
                x = float(x)
            except ValueError:
                print("You wanna try to calculate things other than numbers?"
                      "\nNot on my watch!")
                continue
            x = round(x)
            y = input("Enter the number: ")
            try:
                y = float(y)
            except ValueError:
                print("You wanna try to calculate things other than numbers?"
                      "\nNot on my watch!")
                continue
            y = round(y)
            if op == "+":
                print(f"{x} + {y} = {calc_add(x, y)}")
            elif op == "-":
                print(f"{x} - {y} = {calc_sub(x, y)}")
            elif op == "*":
                print(f"{x} * {y} = {calc_mult(x, y)}")
            elif op == "/":
                if y != 0:
                    print(f"{x} / {y} = {calc_div(x, y)}")
                else:
                    print(calc_div(x, y))
    elif j == "0":
        break
    else:
        print("It is a simple choise...\nDon’t overcomplicate things...")
input("Oh boy, that escalated quickly...")
