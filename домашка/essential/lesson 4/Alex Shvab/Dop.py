def fib(x):
    list = [1, 2]
    for i in range (x):
        list.append(list[i] + list[i+1])
        yield list[i]


def main():
    n = int(input("Enter number: "))
    for i in fib(n):
        print(i)

if __name__ == "__main__":
    main()