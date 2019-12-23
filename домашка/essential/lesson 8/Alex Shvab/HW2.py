import random
import pickle


def gener():
    rand_numb = ""
    with open("rand_numb_binary.txt", "wb") as file:
        for x in range(10000):
            r = str(random.randint(-1000, 1000))
            rand_numb += r + " "
        pickle.dump(rand_numb, file)

def write():
    with open("rand_numb_binary.txt", "rb") as file:
        rand_numb = pickle.load(file)
        print(rand_numb)
        lst = [int(x) for x in rand_numb.split(" ") if x != ""]
        res = 0
        for x in lst:
            res += x
        print(f"{res=}")

gener()
write()