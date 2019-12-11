
def triangle(number):
    for i in range(1, number):
        for j in range(1, number):
            if i >= j: print("{:>2}".format("*"), end="")
        print()
    print()
    for i in range(1, number):
        for j in range(1, number):
            if i <= j: print("{:>2}".format("*"), end="")
        print()

triangle(6)