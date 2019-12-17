while True:
    var = input("Input some words and split by space:\n  ")
    lst = var.split()
    sort = sorted(lst, key=str)
    print(*sort, end=" ")
    end = input("\nAgain? y/n:\n  ")
    if end == "y":
        pass
    elif end == "n":
        break
