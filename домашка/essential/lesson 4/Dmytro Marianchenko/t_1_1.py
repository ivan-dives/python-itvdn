class Revers:
    def __init__(self, some_list, step=1):
        self.some_list = some_list
        self.step = step
        self.new_list = []
        for self.step in self.some_list:
            self.new_list.insert(0, self.step)
        self.some_list = self.new_list

    def __str__(self):
        return str(self.some_list)


def main():
    my_list = []
    while True:
        x = input("Add a number item ('done' to finish or 'exit' to quit):\n>> ")

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
    rev = Revers(my_list)
    print(f"Reversed list: {rev}")


if __name__ == '__main__':
    main()
