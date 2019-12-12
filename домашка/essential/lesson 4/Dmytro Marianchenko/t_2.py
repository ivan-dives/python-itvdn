def gen_rev(some_list):
    x = len(some_list) - 1
    while True:
        try:
            yield some_list[x]
            x -= 1
            if x < 0:
                break
            else:
                pass
        except IndexError:
            raise StopIteration


def main():
    my_list = []
    while True:
        x = input("Add a number or symbol item ('done' to finish or 'exit' to quit):\n>> ")
        if x == "done":
            break
        elif x == "exit":
            exit()
        else:
            if x.isdigit():
                x = int(x)
                my_list.append(x)
            else:
                my_list.append(x)

    print(f"Your list: {my_list}")
    new_list = gen_rev(my_list)
    while True:
        ent = input("If you want to print the last element of your list enter 'y' if not, enter 'not':\n>> ")
        try:
            if ent == "y":
                print(next(new_list))
            elif ent == "not":
                break
        except StopIteration:
            print("It was a last element of your list...")
            exit()


if __name__ == '__main__':
    main()
