
def rectangle(height=4, width=7):
    for i in range(0, height):
        for j in range(0, width):
            print("{:>2}".format("*"), end="")
        print()

rectangle()

print()

for i in range(0, 5):
        print("{:>2}".format("*")*8, end="")
        print()
