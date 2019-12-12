def gen(num_list):
    i = 2
    n = num_list[-1]
    while i <= n:
        if num_list[i] != 0:
            j = i + i
            while j <= n:
                num_list[j] = 0
                j = j + i
        i += 1
    for i in num_list:
        if i > 1:
            try:
                yield i
            except IndexError:
                raise StopIteration


def main():
    num_list = [i for i in range(10000 + 1)]
    num = gen(num_list)
    while True:
        ent = input("If you want to print the next element enter 'y' or 'n' to 'exit':\n>> ")
        try:
            if ent == "y":
                print(next(num))
            elif ent == "n":
                exit()
        except StopIteration:
            print("It was a last element of your list...")
            break
    exit()


if __name__ == '__main__':
    main()
