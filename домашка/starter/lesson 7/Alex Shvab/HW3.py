list = []


def simpl_numb(n):
    for i in range(2, n):
        k = 0
        for j in range (1, i):
            if i % j == 0:
                k = k + 1
        if k < 2:
            list.append(i)


def main():

    x = int(input("Enter end: "))
    simpl_numb(x+1)
    print(f"Simple numbers: {list}")

    while True:
        print("""Enter operation:
        1. Sum
        2. Mult
        3. Exit""")
        op = int(input("> "))
        if op == 1:
            sum = 0
            for i in range( len(list)):
                sum = sum + list[i]
            print(sum)
        elif op == 2:
            sum = 1
            for i in range( len(list)):
                sum = sum * list[i]
            print(sum)
        elif op == 3:
            break

if __name__ == "__main__":
    main()