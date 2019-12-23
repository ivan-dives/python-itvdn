import random


def gener():
    rand_numb = ""
    with open("rand_numb.txt", "w") as file:
        for x in range(10000):
            r = str(random.randint(-1000, 1000))
            rand_numb += r + " "
        file.write(rand_numb)

def write():
    with open("rand_numb.txt", "r") as file:
        rand_numb = file.read()
        print(rand_numb)
        lst = [int(x) for x in rand_numb.split(" ") if x != ""]
        res = 0
        for x in lst:
            res += x
        print(f"{res=}")

gener()
write()