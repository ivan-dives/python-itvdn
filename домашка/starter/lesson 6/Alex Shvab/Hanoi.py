def hanoi(q, a, b, c):
    if q != 0:
        hanoi(q - 1, a, c, b)
        print("Ring from", a, "to", c)
        hanoi(q - 1, b, a, c)



x = int(input("Enter quantity of rings: "))
hanoi(x, "1", "2", "3")